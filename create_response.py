import json
import boto3
def lambda_handler(event, context):
  # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    # current datetime as a potential timestamp attribute
    # event_timestamp = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    question_id = event['resource']
    responses = table.query(KeyConditionExpression=Key('question_id').eq(question_id))
  return
