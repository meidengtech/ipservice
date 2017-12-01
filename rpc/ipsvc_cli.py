import sys

sys.path.insert(0, ".")
sys.path.insert(0, "../")

import grpc
from rpc import ipsvc_pb2_grpc
from rpc import ipsvc_pb2


def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = ipsvc_pb2_grpc.IPSVCStub(channel)
    req = ipsvc_pb2.IPsRequest(ips=[ipsvc_pb2.IPRequest(ip="{i}.{i}.{i}.{i}".format(i=i)) for i in range(256)])
    response = stub.IPSQuery(req)
    for x in response.ipr:
        print(x.ip, x.city, x.loc)


if __name__ == '__main__':
    run()
