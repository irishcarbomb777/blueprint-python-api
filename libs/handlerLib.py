import boto3
import decimal
import json

def handler(fn):
    def func():
        body = fn
        statusCode=200
        return body, statusCode
    body, statusCode = func()
    def replace_decimals(items):
        if isinstance(items, list):
            return [replace_decimals(i) for i in items]
        elif isinstance(items, dict):
            return {k: replace_decimals(v) for k, v in items.items()}
        elif isinstance(items, decimal.Decimal):
            return int(items) if items % 1 == 0 else items
        return items

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


    
