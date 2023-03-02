all: python

python:
	@echo "--> Generating Python client files"
	python3 -m grpc_tools.protoc -I protos/rpc/ --python_out=./rpc/ --grpc_python_out=./rpc/ protos/rpc/ipsvc.proto
	@echo ""

# golang:
# 	@echo "--> Generating Go files"
# 	protoc -I protos/ --go_out=plugins=grpc:protobuf/ protobuf/primefactor.proto
# 	@echo ""

install:
	@echo "--> Installing Python grpcio tools"
	pip3 install -U grpcio grpcio-tools
	@echo ""
