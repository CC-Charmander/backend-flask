from flask import Flask, jsonify
from flask_cors import CORS
import boto3
import os
from src.main.routes import register_routes  # ルート登録関数をインポート

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Bedrock クライアントをアプリコンテキストに登録
    app.bedrock_client = boto3.client(
        "bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )

    register_routes(app)

    # カスタムエラーハンドラー
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found"}), 404


    return app

app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=8000, debug=debug_mode)
