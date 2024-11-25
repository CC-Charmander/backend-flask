import boto3
import json


bedrock_client = boto3.client("bedrock-runtime",region_name="us-east-1")

body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "system": "あなたの仕事はユーザーの質問に答えることです。",
        "messages": [
            {
                "role": "user",
                "content": "雲の上には何がありますか？"
            }
        ]
    }
)

bedrock_model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

header_accept = "application/json"
content_type = "application/json"

res = bedrock_client.invoke_model(
    body=body,
    modelId=bedrock_model_id,
    accept=header_accept,
    contentType=content_type
)

if res.get("body"):
    res_body = json.loads(res.get("body").read())

    if res_body["content"]:
        answer = res_body["content"][0].get("text")
        print(answer)
else:
    print("レスポンスのボディがありません！")