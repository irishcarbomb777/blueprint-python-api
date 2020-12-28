from libs.handlerLib import handler
from libs.dynamodbLib import dynamoDb

def main(event, context):
    def func(event, context):
        return event
    
    return handler(func(event, context))