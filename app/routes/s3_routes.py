from flask import request, Blueprint, jsonify
import requests

from ..utils.aws_connection import s3_connection, sns_connection

api_blueprint = Blueprint('api', __name__)

# object_key =  'files/test.txt'
bucket_name =  "mysas3bucketforyou"

@api_blueprint.route('/list_buckets', methods=['GET'])
def list_buckets():
    connection = s3_connection()
    print(f" connection established ")

    data = connection.list_buckets()

    print(f" buckets {data['Buckets']}")

    return jsonify({"message": f"buckets: {data['Buckets']}"}), 201


@api_blueprint.route('/upload_file', methods=['POST'])
def upload_file():
    s3_conn = s3_connection()
    print(f" connection established ")

    s3_conn.upload_file("sai.jpg", bucket_name, 'sai.jpg')

    print(f" Upload Successful ")

    public_url=f"https://{bucket_name}.s3.us-east-1.amazonaws.com/sai.jpg"

    sns_conn = sns_connection()

    sns_conn.publish(
        TopicArn='arn:aws:sns:us-east-1:979907616055:Email-Me',
        Subject='File Uploaded TESTING!!',
        Message=f'Access the file using this url {public_url}'
    )

    return jsonify({"message": f"File uploaded url to access data: {public_url}"}), 201

@api_blueprint.route('/get_file', methods=['GET'])
def access_file():
    request_data = request.get_json()

    print(f"request data: {request_data}")

    url_data = requests.get(request_data['url'])

    with open('new_file.jpg', "wb") as f:
        f.write(url_data.content)

    return jsonify({"message": f"data accessed: {url_data}"}), 201


@api_blueprint.route('/update_file', methods=['PUT'])
def update_file():
    conn = s3_connection()

    with open('sai.jpg', "rb") as f:
        conn.put_object(Bucket=bucket_name, Key='tweety.jpeg', Body=f)

    public_url=f"https://{bucket_name}.s3.us-east-1.amazonaws.com/tweety.jpeg"

    return jsonify({"message": f"data updated: url: {public_url}"}), 201


@api_blueprint.route('/delete_file', methods=['DELETE'])
def delete_file():
    conn = s3_connection()

    conn.delete_object(Bucket=bucket_name, Key='bunny.jpeg')


    return jsonify({"message": f"data deleted"}), 201