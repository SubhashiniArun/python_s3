import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def s3_connection():
    print("Establishing S3 connection!!")

    client = boto3.client('s3',
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                          region_name='us-east-1'
                          )
    print('Established S3 connection')
    return client

def sns_connection():
    sns_client = boto3.client('sns',
                            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                            region_name='us-east-1'
                            )
    print('Established SNS connection')
    return sns_client