import boto3
import json
from .createPrompt import createSnackPrompt

def getSnacks(value, bedrock_client):

    #bedrock_client = boto3.client("bedrock-runtime",region_name="us-east-1")

    text = createSnackPrompt(value)
    print(text)

    systemPrompt = text[0]
    prompt = text[1]

    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "system": systemPrompt,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    # bedrock_model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    bedrock_model_id = "anthropic.claude-3-5-haiku-20241022-v1:0"

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
            return answer
    else:
        return "レスポンスのボディがありません！"