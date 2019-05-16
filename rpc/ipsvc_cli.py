import sys
import argparse
import os.path
sys.path.insert(0, os.path.abspath("."))

import grpc
from rpc import ipsvc_pb2_grpc
from rpc import ipsvc_pb2


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--server',
        dest="server",
        help='server addr',
        default="127.0.0.1:9000",
        type=str)
    args = parser.parse_args()

    channel = grpc.insecure_channel(args.server)
    stub = ipsvc_pb2_grpc.IPSVCStub(channel)

    req = ipsvc_pb2.IPsRequest(ips=[
        ipsvc_pb2.IPRequest(ip="{i}.{i}.{i}.{i}".format(i=i))
        for i in range(256)
    ])
    response = stub.IPSQuery(req)
    for x in response.ipr:
        print(x.ip, x.city, x.loc)

    val = [ipsvc_pb2.IPRequest(ip=".".join([str(i)] * 4)) for i in range(255)]

    resp = stub.IPStreamQuery(iter(val))
    for x in resp:
        print(x.ip, x.city, x.loc)


if __name__ == '__main__':
    run()
