import json
import numpy as np
def hello(event, context):
  body = {
    "message": "Go Serverless v1.0! Your function executed successfully!",
  }

  return {
      "statusCode": 200,
      "body": json.dumps(body)
  }

def numpyTest(event, context):
  a = np.arange(5)
  b = a[2]

  body = {
    "number": int(b)
  }

  return {
    "statusCode" : 200,
    "body" : json.dumps(body)
  }

