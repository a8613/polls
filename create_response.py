import json
import boto3
def lambda_handler(event, context):
  # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table questions object
    questions_table = dynamodb.Table('questions')
    
    # capturing question_id and returning responses for that question
    question_id = event['resource']
    question = questions_table.get_item(
           Key={
               'question_id': question_id
           }
        )   
    responses = question['responses']
    
  return responses
