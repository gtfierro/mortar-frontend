package main

import (
	"context"
	"fmt"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	mortarproto "github.com/gtfierro/mortar/proto"
	logrus "github.com/sirupsen/logrus"
	"google.golang.org/grpc"
	"net"
	"net/http"
	"os"
	"strings"
	"time"
)

func init() {
	logrus.SetFormatter(&logrus.TextFormatter{FullTimestamp: true, ForceColors: true})
	logrus.SetOutput(os.Stdout)
	logrus.SetLevel(logrus.DebugLevel)
}

type MortarAPI struct {
	hodaddress string
	hod        mortarproto.HodDBClient

	sites []string

	mux *runtime.ServeMux
}

type Config struct {
	HodAddress string
	Port       int
}

func NewMortarAPI(cfg *Config) (*MortarAPI, error) {
	api := &MortarAPI{
		hodaddress: cfg.HodAddress,
	}
	opts := []grpc.DialOption{grpc.WithInsecure(), grpc.WithBlock(), grpc.FailOnNonTempDialError(true)} //, grpc.WithTransportCredentials(credentials.NewTLS(&tls.Config{}))}
	hodconn, err := grpc.Dial(cfg.HodAddress, opts...)
	if err != nil {
		return nil, err
	}
	api.hod = mortarproto.NewHodDBClient(hodconn)

	// query for all sites
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Minute)
	defer cancel()
	resp, err := api.hod.ExecuteQuery(ctx, &mortarproto.QueryRequest{
		Query: "LIST VERSIONS AT now;",
	})
	if err != nil {
		return nil, err
	}
	for _, row := range resp.Rows {
		api.sites = append(api.sites, row.Uris[0].Value)
	}
	logrus.Infof("Got %d sites", len(api.sites))

	//	resp, err = api.hod.ExecuteQuery(ctx, &mortarproto.QueryRequest{
	//		Query: "SELECT ?equip ?equiptype ?point ?pointtype WHERE { ?equip bf:hasPoint ?point . ?equip rdf:type ?equiptype . ?point rdf:type ?pointtype};",
	//	})
	//	if err != nil {
	//		return nil, err
	//	}
	//	for _, row := range resp.Rows {
	//		logrus.Warning(row)
	//	}

	// start grpc server
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", cfg.Port))
	if err != nil {
		return nil, err
	}
	grpcServer := grpc.NewServer()
	mortarproto.RegisterMortarServer(grpcServer, api)
	go grpcServer.Serve(lis)

	api.mux = runtime.NewServeMux()
	err = mortarproto.RegisterMortarHandlerFromEndpoint(context.Background(), api.mux, fmt.Sprintf(":%d", cfg.Port), opts)
	if err != nil {
		return nil, err
	}

	return api, nil
}

func (api *MortarAPI) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	api.mux.ServeHTTP(w, r)
}

func (api *MortarAPI) Qualify(ctx context.Context, request *mortarproto.QualifyRequest) (*mortarproto.QualifyResponse, error) {
	var sites = make(map[string]struct{})
	var response = new(mortarproto.QualifyResponse)
	// do all mandatory queries
	logrus.Infof("Qualify query %v", request)
	for _, reqquery := range request.Requiredqueries {
		for _, sitename := range api.sites {
			newq := strings.Replace(reqquery.Query, "WHERE", fmt.Sprintf("FROM %s WHERE", sitename), 1)
			newreq := &mortarproto.QueryRequest{Query: newq}
			resp, err := api.hod.ExecuteQuery(ctx, newreq)
			if err != nil {
				response.Error = err.Error()
				return response, err
			}
			if resp.Count > 0 {
				sites[sitename] = struct{}{}
			} else {
				delete(sites, sitename)
			}
		}
	}

	// handle optional?
	if len(request.Optionalqueries) > 0 {
		for sitename := range sites {
			qualified := false
			for _, optquery := range request.Optionalqueries {
				newq := strings.Replace(optquery.Query, "WHERE", fmt.Sprintf("FROM %s WHERE", sitename), 1)
				newreq := &mortarproto.QueryRequest{Query: newq}
				resp, err := api.hod.ExecuteQuery(ctx, newreq)
				if err != nil {
					response.Error = err.Error()
					return response, err
				}
				if !qualified {
					qualified = resp.Count > 0
				}
			}
			if !qualified {
				delete(sites, sitename)
			}
		}
	}

	for sitename := range sites {
		response.Sites = append(response.Sites, sitename)
	}

	return response, nil
}
