package main

import (
	"context"
	_ "crypto/tls"
	"fmt"
	"log"
	"net/http"
	//"strings"

	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	mdalgrpc "github.com/gtfierro/mdal/proto"
	"github.com/rs/cors"
	//"golang.org/x/crypto/acme/autocert"
	"google.golang.org/grpc"
	//"google.golang.org/grpc/credentials"
	"github.com/jinzhu/gorm"
	_ "github.com/mattn/go-sqlite3"
	"github.com/qor/admin"
	_ "github.com/qor/qor"
	_ "google.golang.org/grpc/encoding/gzip"
)

// Create a GORM-backend model
type User struct {
	gorm.Model
	Name   string
	APIKey string
}

func main() {
	DB, _ := gorm.Open("sqlite3", "demo.db")
	DB.AutoMigrate(&User{})

	// Initalize
	Admin := admin.New(&admin.AdminConfig{DB: DB})

	// Allow to use Admin to manage User
	Admin.AddResource(&User{})

	// initalize an HTTP request multiplexer
	mux := http.NewServeMux()

	// Mount admin interface to mux
	Admin.MountTo("/admin", mux)

	// initialize GRPC proxy
	_ = cors.New(cors.Options{
		AllowedOrigins:   []string{"*"},
		AllowedMethods:   []string{"GET", "POST"},
		AllowCredentials: true,
		Debug:            true,
	})

	grpcmux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure(), grpc.WithBlock(), grpc.FailOnNonTempDialError(true)} //, grpc.WithTransportCredentials(credentials.NewTLS(&tls.Config{}))}
	//&tls.Config{}
	if err := mdalgrpc.RegisterMDALHandlerFromEndpoint(context.Background(), grpcmux, "corbusier.cs.berkeley.edu:8088", opts); err != nil {
		log.Fatal(err)
		panic(err)
	}

	static := http.FileServer(http.Dir("static"))

	// GRPC gateway expects to be mounted on /, but we also want to
	// serve our files from the same port. This handler hands the request
	// off to the correct mux. In the future, we may want a more robust
	// method of determining which endpoint the request should go to
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/v1/mdal/query" {
			grpcmux.ServeHTTP(w, r)
		} else {
			static.ServeHTTP(w, r)
		}
	})

	fmt.Println("Listening on: 9000")

	//m := autocert.Manager{
	//	Prompt:     autocert.AcceptTOS,
	//	HostPolicy: autocert.HostWhitelist("0.0.0.0:9000"),
	//	Cache:      autocert.DirCache("certs"),
	//}
	//_ = m
	//srv := &http.Server{
	//	Addr:    "0.0.0.0:9000",
	//	Handler: mux,
	//	//TLSConfig: &tls.Config{GetCertificate: m.GetCertificate},
	//}
	//srv.ListenAndServeTLS("", "")
	//select {}
	http.ListenAndServe(":9000", mux)
}
