from libs.handlerLib import handler
from libs.dynamodbLib import dynamoDb

def main(event, context):
    def fn(event, context):
        return event
    
    return handler(fn(event, context))