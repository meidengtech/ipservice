from flask import Flask, request, jsonify, current_app
from extra.czip import loadXdb


def ips_parser(s: str):
    T = [x for x in s.split("|") if x!="0"]
    return [" ".join(T[0:-1]),T[-1]]

def create_app():
    app1 = Flask(__name__)
    app1.ipq = loadXdb()

    @app1.route("/q", methods=["GET", "POST"])
    def query():
        ips = request.values.get("ips", "127.0.0.1")
        res = [(ip, ips_parser(current_app.ipq.search(ip))) for ip in ips.split(",") if ip]
        return jsonify(success=1, ret=dict(res))

    @app1.errorhandler(404)
    def page_not_found(e):
        return jsonify(success=0, msg="page not found", err=e), 404

    return app1


app = create_app()
