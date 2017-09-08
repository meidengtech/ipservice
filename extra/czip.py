import sys
from qqwry import QQwry
from .config import IP_DATA_FILE


def load_qqwry():
    ipq = QQwry()
    res = ipq.load_file(IP_DATA_FILE, loadindex=True)
    if not res:
        print("qqwry load failed", IP_DATA_FILE)
        sys.exit(-1)
    return ipq
