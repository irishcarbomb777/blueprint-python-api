import boto3
import decimal
import json

def handler(fn):
    def func():
        body = fn
        statusCode=200
        return body, statusCode
    body, statusCode = func()
    # This below function is required to deal with json packages lack of decimal
    # handling (dynamodb returns all numbers as decimals)
    def replace_decimals(items):
        if isinstance(items, list):
            return [replace_decimals(i) for i in items]
        elif isinstance(items, dict):
            return {k: replace_decimals(v) for k, v in items.items()}
        elif isinstance(items, decimal.Decimal):
            return int(items) if items % 1 == 0 else items
        return items
    # This below function is required to convert the items object to lists as opposed
    # to sets. Json is a js based function and does not know how to deal with
    # set type objects
    def set_default(obj):
        if isinstance(obj, set):
            return(list(obj))
        raise TypeError    
    body = replace_decimals(body)
    body = json.dumps(body, default=set_default)
    return {
        "statusCode": 200,
        "body" : body

    }


    
