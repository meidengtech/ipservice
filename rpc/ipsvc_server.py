import sys
import os.path
import argparse
import logging
import signal

sys.path.insert(0, os.path.abspath("."))

from concurrent import futures
import time
import grpc
from extra.czip import loadXdb
from rpc import ipsvc_pb2
from rpc import ipsvc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_GRACE_STOP_SECONDS = 60
ipq = loadXdb()

def ips_parser(s: str):
    T = [x for x in s.split("|") if x!="0"]
    return [" ".join(T[0:-1]),T[-1]]


def query_one_ip(ip):
    resp = ips_parser(ipq.search(ip))
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
        return ipsvc_pb2.IPsReply(
            ipr=[self.IPQuery(ip, context) for ip in ips])

    def IPStreamQuery(self, request_iterator, context):
        for req in request_iterator:
            ip = req.ip
            # print("streaming {}".format(ip))
            yield ipsvc_pb2.IPReply(**query_one_ip(ip))


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--bind', dest="bind", help='bind', default=":8000", type=str)
    parser.add_argument(
        '-w',
        '--workers',
        dest='worker_num',
        help='worker numbers',
        default=10,
        type=int)
    args = parser.parse_args()
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=args.worker_num))
    ipsvc_pb2_grpc.add_IPSVCServicer_to_server(IPSvc(), server)
    server.add_insecure_port(args.bind)
    server.start()
    logging.warn("service started at {}".format(args.bind))

    def signal_term_handler(signal, frame):
        logging.warn('got SIGTERM beg')
        server.stop(_GRACE_STOP_SECONDS)
        logging.warn('got SIGTERM end')
        sys.exit(0)

    signal.signal(signal.SIGTERM, signal_term_handler)
    signal.signal(signal.SIGINT, signal_term_handler)

    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)


if __name__ == '__main__':
    serve()
