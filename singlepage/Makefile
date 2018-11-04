.PHONY: proto

GOPATH = /home/gabe/go

run: build
	./mortar

proto: proto/mortar.proto
	protoc -Iproto/ -I ${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis -I${GOPATH}/src/github.com/dan-compton --go_out=plugins=grpc:proto proto/*.proto
	protoc -I/usr/local/include -Iproto/ -I${GOPATH}/src -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis -I${GOPATH}/src/github.com/dan-compton --grpc-gateway_out=logtostderr=true:proto proto/*.proto
	protoc -I/usr/local/include -Iproto/ -I${GOPATH}/src -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis -I${GOPATH}/src/github.com/dan-compton --swagger_out=logtostderr=true:proto proto/*.proto
	python -m grpc_tools.protoc -Iproto -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --python_out=proto --grpc_python_out=proto proto/*.proto

build: 
	go build
