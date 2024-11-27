from flask import Flask, jsonify, request
from src.service.getSnacks import getSnacks
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)

bedrock_client = boto3.client("bedrock-runtime",region_name="us-east-1")

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask in AWS Lambda!")

@app.route('/test')
def test():
    param = request.get_json()
    return param

@app.route('/api/snack', methods=["GET"])
def getSnack():
    # param = request.get_json()
    param = request.args.get("ingredients")

    return getSnacks(param, bedrock_client)
    #return param

@app.route('/api/snack/test', methods=["GET"])
def getSnackTest():
    
    return getSnacks("ジン", bedrock_client)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)