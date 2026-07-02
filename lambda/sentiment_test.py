import os
import requests
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&language=en"

data = requests.get(url).json()

for article in data["results"][:5]:
    title = article["title"]

score = TextBlob(title).sentiment.polarity