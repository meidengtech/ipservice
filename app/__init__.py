from flask import Flask, request, jsonify
from extra.czip import load_qqwry

ipq = None
app = Flask(__name__)


@app.before_first_request
def app_first():
    global ipq
    if not ipq:
        ipq = load_qqwry()


@app.route("/q", methods=["GET", "POST"])
def query():
    ips = request.values.get("ips")
    res = [(ip, ipq.lookup(ip)) for ip in ips.split(",")]
    return jsonify(success=1, ret=dict(res))
