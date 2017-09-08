import sys

from qqwry import updateQQwry

from extra.czip import IP_DATA_FILE


def init():
    result = updateQQwry(IP_DATA_FILE)
    if result < 0:
        print("Update File Error: ", result)
        sys.exit(result)
    else:
        print("File Load Successfully: ", result)
