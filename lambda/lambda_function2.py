import json
import boto3
import psycopg2
from textblob import TextBlob
import os

load_dotenv()

print("Lambda started")

s3 = boto3.client("s3")