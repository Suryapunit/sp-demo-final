import json

def lambda_handler(event, context):
    # TODO implement
    print("Hello,World!")
    print("What's up?")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
