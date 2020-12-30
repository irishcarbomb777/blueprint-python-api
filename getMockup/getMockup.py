from libs.handlerLib import handler
from libs.dynamodbLib import dynamoDb
def main(event, context):
    def fn(event, context):
        call = dynamoDb['get']
        response = call(
            Key = {
                'itemId': event['queryStringParameters']['itemId'],
                'imprintId': event['queryStringParameters']['imprintId']
            }
        )
        return response['Item']
    return handler(fn(event, context))







