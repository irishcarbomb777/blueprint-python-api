import boto3
import decimal
import json

def handler(lamb):
    # Change decimals to int for JSON 
    def replace_decimals(items):
        if isinstance(items, list):
            return [replace_decimals(i) for i in items]
        elif isinstance(items, dict):
            return {k: replace_decimals(v) for k, v in items.items()}
        elif isinstance(items, decimal.Decimal):
            return int(items) if items % 1 == 0 else items
        return items
    # Convert object to list. JSON cannot read set objects
    def set_default(obj):
        if isinstance(obj, set):
            return(list(obj))
        raise TypeError
    # Run your passed in lambda function
    def fn():
        body = lamb
        return body
    
    try:
        body= fn()   
        body = replace_decimals(body)
        body = json.dumps(body, default=set_default)
        statusCode = 200
    except Exception as error:
        errors = error.args
        body = json.dumps(errors)
        statusCode = 500


    return {
        "statusCode" : statusCode,
        "body"       : body,
        "headers"    : {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True
        }
    }


    
