# Python S3, SNS Project

-> Upload, get, update, delete files in AWS S3 bucket using boto3 module

-> AWS SNS is to used to send notifications on file upload
* create topic under SNS
* create subscribtion with required email_ids as endpoints, set EMAIL as protocol

* Make sure necessary S3 bucket permissions, SNS permissions are added to AWS user
SNS permissions (Publish, Susbcribe)