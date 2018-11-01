// Code generated by protoc-gen-grpc-gateway. DO NOT EDIT.
// source: proto/mdal.proto

/*
Package mdalgrpc is a reverse proxy.

It translates gRPC into RESTful JSON APIs.
*/
package proto

import (
	"io"
	"net/http"

	"github.com/golang/protobuf/proto"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"github.com/grpc-ecosystem/grpc-gateway/utilities"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/grpclog"
	"google.golang.org/grpc/status"
)

var _ codes.Code
var _ io.Reader
var _ status.Status
var _ = runtime.String
var _ = utilities.NewDoubleArray

func request_MDAL_DataQuery_0(ctx context.Context, marshaler runtime.Marshaler, client MDALClient, req *http.Request, pathParams map[string]string) (MDAL_DataQueryClient, runtime.ServerMetadata, error) {
	var protoReq DataQueryRequest
	var metadata runtime.ServerMetadata

	if err := marshaler.NewDecoder(req.Body).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	stream, err := client.DataQuery(ctx, &protoReq)
	if err != nil {
		return nil, metadata, err
	}
	header, err := stream.Header()
	if err != nil {
		return nil, metadata, err
	}
	metadata.HeaderMD = header
	return stream, metadata, nil

}

// RegisterMDALHandlerFromEndpoint is same as RegisterMDALHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterMDALHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.Dial(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterMDALHandler(ctx, mux, conn)
}

// RegisterMDALHandler registers the http handlers for service MDAL to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterMDALHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterMDALHandlerClient(ctx, mux, NewMDALClient(conn))
}

// RegisterMDALHandlerClient registers the http handlers for service MDAL
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "MDALClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "MDALClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "MDALClient" to call the correct interceptors.
func RegisterMDALHandlerClient(ctx context.Context, mux *runtime.ServeMux, client MDALClient) error {

	mux.Handle("POST", pattern_MDAL_DataQuery_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		if cn, ok := w.(http.CloseNotifier); ok {
			go func(done <-chan struct{}, closed <-chan bool) {
				select {
				case <-done:
				case <-closed:
					cancel()
				}
			}(ctx.Done(), cn.CloseNotify())
		}
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_MDAL_DataQuery_0(rctx, inboundMarshaler, client, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_MDAL_DataQuery_0(ctx, mux, outboundMarshaler, w, req, func() (proto.Message, error) { return resp.Recv() }, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_MDAL_DataQuery_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0, 2, 1, 2, 2}, []string{"v1", "mdal", "query"}, ""))
)

var (
	forward_MDAL_DataQuery_0 = runtime.ForwardResponseStream
)
