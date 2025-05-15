import json
import boto3
import os

topic_arn = os.environ['SNS_TOPIC_ARN']
sns_client = boto3.client('sns')


def lambda_handler(event, context):
    print(f"event: {event}")
    for record in event['Records']:
        print(f"record: {record}")
        bucket_name = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        public_url=f"https://{bucket_name}.s3.us-east-1.amazonaws.com/{key}"

        message = f"Access the file using this url {public_url}"
    
    
    sns_client.publish(TopicArn=topic_arn, Message=f"file uploaded! {message}", Subject='New file uploaded')


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
