from libs.handlerLib import handler
from libs.dynamodbLib import dynamoDb
def main(event, context):
    def func(event, context):
        call = dynamoDb['get']
        response = call(
            Key = {
                'itemId': event['queryStringParameters']['itemId'],
                'imprintId': event['queryStringParameters']['imprintId']
            }
        )
        return response['Item']
    return handler(func(event, context))







