from flask import Flask, request, jsonify, current_app
from extra.czip import load_qqwry


def create_app():
    app1 = Flask(__name__)
    app1.ipq = load_qqwry()

    @app1.route("/q", methods=["GET", "POST"])
    def query():
        ips = request.values.get("ips", "127.0.0.1")
        res = [(ip, current_app.ipq.lookup(ip)) for ip in ips.split(",") if ip]
        return jsonify(success=1, ret=dict(res))

    @app1.errorhandler(404)
    def page_not_found(e):
        return jsonify(success=0, msg="page not found"), 404

    return app1


app = create_app()
