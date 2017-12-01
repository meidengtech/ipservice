import sys

sys.path.insert(0, ".")
sys.path.insert(0, "../")

from concurrent import futures
import time
import grpc
from extra.czip import load_qqwry
from rpc import ipsvc_pb2
from rpc import ipsvc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
ipq = load_qqwry()


def query_one_ip(ip):
    resp = ipq.lookup(ip) or ['', '']
    city, loc = tuple(resp[:2])

    if loc.strip() == "CZ88.NET":
        loc = "__"

    return dict(ip=ip, city=city, loc=loc)


class IPSvc(ipsvc_pb2_grpc.IPSVCServicer):
    def IPQuery(self, request, context):
        ip = request.ip
        return ipsvc_pb2.IPReply(**query_one_ip(ip))

    def IPSQuery(self, request, context):
        ips = request.ips
        return ipsvc_pb2.IPsReply(ipr=[self.IPQuery(ip, context) for ip in ips])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ipsvc_pb2_grpc.add_IPSVCServicer_to_server(IPSvc(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
