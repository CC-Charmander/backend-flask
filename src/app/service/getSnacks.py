import boto3
import json

def getSnacks():
    bedrock = boto3.client(service_name='bedrock-runtime')

    text = f"カシスリキュールが材料のおすすめカクテルを教えて"

    #titanのbody
    body = json.dumps({
        "inputText": text,
        "textGenerationConfig": {
            "temperature": 0.7,
            "topP": 0.9,
            "maxTokenCount": 300
        }
    })

    #モデルなどを指定し、bedrockにリクエスト
    response = bedrock.invoke_model(
        body = body,
        modelId = "amazon.titan-text-express-v1",
        accept = 'application/json',
        contentType = 'application/json'
        )

    #titanのoutput
    response_body = json.loads(response.get('body').read())
    output_text = response_body['results'][0]['outputText']
    
    return output_text