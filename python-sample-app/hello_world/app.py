import json
import traceback

def main_func():

    # Force an exception. For Testing
    a=10
    if a == 10:
        raise Exception("Date provided can't as an arraylist")
    
    return {
        "statusCode": 503,
        "body": json.dumps(
            {
                "message": "hello world: app error",
            }
        ),
    }

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        return main_func()
    except Exception as err:
        print(err)
        traceback.print_exc()
    
