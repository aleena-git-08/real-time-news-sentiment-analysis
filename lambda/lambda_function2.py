import json
import boto3
import psycopg2
from textblob import TextBlob
import os

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

    print("Connecting to RDS...")

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST1"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD1"),
        port=os.getenv("DB_PORT")
    )

    print("Connected to RDS")

    cur = conn.cursor()

    for article in data["results"][:10]:

        title = article.get("title")

        if not title:
            continue

        score = TextBlob(title).sentiment.polarity

        if score > 0:
            sentiment = "Positive"
        elif score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        cur.execute(
            """
            INSERT INTO news_data(title,sentiment)
            VALUES(%s,%s)
            """,
            (title, sentiment)
        )

    conn.commit()

    print("Committed")

    cur.close()
    conn.close()

    print("Finished")

    return {
        "statusCode": 200
    }