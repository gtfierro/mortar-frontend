package main

import (
	"context"
	"fmt"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"github.com/gtfierro/mortar/proto"
	"github.com/pkg/errors"
	logrus "github.com/sirupsen/logrus"
	"google.golang.org/grpc"
	"net"
	"net/http"
	"os"
	"strings"
	"sync"
	"time"
)

func init() {
	logrus.SetFormatter(&logrus.TextFormatter{FullTimestamp: true, ForceColors: true})
	logrus.SetOutput(os.Stdout)
	logrus.SetLevel(logrus.DebugLevel)
}

type MortarAPI struct {
	hodaddress string
	hod        proto.HodDBClient
	mdal       proto.MDALClient

	sites []string
	// map to uuids
	pointnames sync.Map

	mux *runtime.ServeMux
}

type Config struct {
	HodAddress  string
	MdalAddress string
	Port        int
}

func NewMortarAPI(cfg *Config) (*MortarAPI, error) {
	api := &MortarAPI{
		hodaddress: cfg.HodAddress,
	}
	opts := []grpc.DialOption{grpc.WithInsecure(), grpc.WithBlock(), grpc.FailOnNonTempDialError(true), grpc.WithDefaultCallOptions(grpc.MaxCallRecvMsgSize(100*1024*1024), grpc.MaxCallSendMsgSize(100*1024*1024))} //, grpc.WithTransportCredentials(credentials.NewTLS(&tls.Config{}))}
	hodconn, err := grpc.Dial(cfg.HodAddress, opts...)
	if err != nil {
		return nil, err
	}
	api.hod = proto.NewHodDBClient(hodconn)

	// query for all sites
	logrus.Infof("Loading in sites")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
	defer cancel()
	resp, err := api.hod.ExecuteQuery(ctx, &proto.QueryRequest{
		Query: "LIST VERSIONS AT now;",
	})
	if err != nil {
		return nil, err
	}
	for _, row := range resp.Rows {
		sitename := row.Uris[0].Value
		api.sites = append(api.sites, sitename)
		// load in UUIDs
		resp, err = api.hod.ExecuteQuery(ctx, &proto.QueryRequest{
			Query: fmt.Sprintf("SELECT ?pointname ?uuid FROM %s WHERE { ?pointname bf:uuid ?uuid };", sitename),
		})
		if err != nil {
			logrus.Error(sitename, " ", err)
			continue
		}
		for _, uuidrow := range resp.Rows {
			api.pointnames.Store(uuidrow.Uris[0].Value, uuidrow.Uris[1].Value)
		}

	}
	logrus.Infof("Got %d sites", len(api.sites))

	logrus.Infof("Connecting to MDAL at %s", cfg.MdalAddress)
	mdalconn, err := grpc.Dial(cfg.MdalAddress, opts...)
	if err != nil {
		return nil, err
	}
	api.mdal = proto.NewMDALClient(mdalconn)
	logrus.Infof("Connected to MDAL at %s", cfg.MdalAddress)

	//	resp, err = api.hod.ExecuteQuery(ctx, &proto.QueryRequest{
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
	proto.RegisterMortarServer(grpcServer, api)
	go grpcServer.Serve(lis)

	api.mux = runtime.NewServeMux()
	err = proto.RegisterMortarHandlerFromEndpoint(context.Background(), api.mux, fmt.Sprintf(":%d", cfg.Port), opts)
	if err != nil {
		return nil, err
	}

	return api, nil
}

func (api *MortarAPI) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	api.mux.ServeHTTP(w, r)
}

func (api *MortarAPI) Qualify(ctx context.Context, request *proto.QualifyRequest) (*proto.QualifyResponse, error) {
	var sites = make(map[string]struct{})
	var response = new(proto.QualifyResponse)
	// do all mandatory queries
	logrus.Infof("Qualify query %v", request)
	for _, reqquery := range request.Requiredqueries {
		for _, sitename := range api.sites {
			newq := strings.Replace(reqquery.Query, "WHERE", fmt.Sprintf("FROM %s WHERE", sitename), 1)
			newreq := &proto.QueryRequest{Query: newq}
			resp, err := api.hod.ExecuteQuery(ctx, newreq)
			if err != nil {
				response.Error = err.Error()
				//return response, err
				continue
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
				newreq := &proto.QueryRequest{Query: newq}
				resp, err := api.hod.ExecuteQuery(ctx, newreq)
				if err != nil {
					response.Error = err.Error()
					//return response, err
					continue
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

func (api *MortarAPI) Fetch(ctx context.Context, request *proto.FetchRequest) (*proto.FetchResponse, error) {
	var response = new(proto.FetchResponse)

	receiver, err := api.mdal.DataQuery2(ctx, request.Request)
	if err != nil {
		response.Error = err.Error()
		return response, errors.Wrap(err, "could not do dataquery")
	}
	resp, err := receiver.Recv()

	response.Response = resp
	if err != nil {
		response.Error = err.Error()
	}
	return response, err
}
