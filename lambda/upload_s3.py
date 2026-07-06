import boto3
import requests
import json
import os

API_KEY = os.getenv("API_KEY")

url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&language=en"

data = requests.get(url).json()

s3 = boto3.client("s3")

s3.put_object(
    Bucket="news-storage-bucket-1",
    Key="news.json",
    Body=json.dumps(data)
)