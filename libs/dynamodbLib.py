import boto3

x = boto3.resource('dynamodb')
client   = boto3.client('dynamodb')
table    = x.Table('mockupgenerator')

dynamoDb = {
    "get": table.get_item,
    "put": table.put_item,
    "query": table.query,
    "update": table.update_item,
    "delete": table.delete_item
}