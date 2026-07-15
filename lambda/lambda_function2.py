import json
import boto3
import psycopg2
from textblob import TextBlob
import os

load_dotenv()

print("Lambda started")

s3 = boto3.client("s3")

def lambda_handler(event, context):

    print("Reading S3 event")

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(bucket)
    print(key)

    response = s3.get_object(Bucket=bucket, Key=key)

    print("S3 object downloaded")

    data = json.loads(response['Body'].read())