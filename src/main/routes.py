from flask import jsonify, request, Blueprint
from src.service.getSnacks import getSnacks

def register_routes(app):
    @app.route('/')
    def hello():
        return jsonify(message="Hello from Flask in AWS Lambda!")

    @app.route('/test')
    def test():
        param = request.get_json()
        return param

    @app.route('/api/snack', methods=["GET"])
    def getSnack():
        param = request.args.get("ingredients")
        bedrock_client = app.bedrock_client  # current_app ではなく app を使用
        return getSnacks(param, bedrock_client)

    @app.route('/api/snack/test', methods=["GET"])
    def getSnackTest():
        bedrock_client = app.bedrock_client  # current_app ではなく app を使用
        return getSnacks("ジン", bedrock_client)
