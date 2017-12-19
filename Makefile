all: python

python:
	@echo "--> Generating Python client files"
	python3 -m grpc_tools.protoc -I protos/ --python_out=./rpc/ --grpc_python_out=./rpc/ protos/ipsvc.proto
	@echo ""

golang:
	@echo "--> Generating Go files"
	protoc -I protobuf/ --go_out=plugins=grpc:protobuf/ protobuf/primefactor.proto
	@echo ""

install:
	@echo "--> Installing Python grpcio tools"
	pip3 install -U grpcio grpcio-tools
	@echo ""
