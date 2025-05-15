# Python S3, SNS Project

-> Upload, get, update, delete files in AWS S3 bucket using boto3 module

-> AWS SNS is to used to send notifications on file upload
* create topic under SNS
* create subscribtion with required email_ids as endpoints, set EMAIL as protocol

* Make sure necessary S3 bucket permissions, SNS permissions are added to AWS user
SNS permissions (Publish, Susbcribe)

Set up AWS Lambda function to send out email notifications to users 
Lambda
-> Create lambda function, see the file *lambda_handler.py* in utils folder
-> set the lambda execution role to Allow -> Sns:Publish for that topic_arn
-> set the topic_arn as environment variable

S3 bucket
-> In Bucket properties, create an event notification for created lambda function