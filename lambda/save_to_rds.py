import requests
import psycopg2
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST1"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD1"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&language=en"

data = requests.get(url).json()

for article in data["results"][:10]:

    title = article["title"]

    score = TextBlob(title).sentiment.polarity

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    cur.execute(
        "INSERT INTO news_data(title, sentiment) VALUES (%s, %s)",
        (title, sentiment)
    )