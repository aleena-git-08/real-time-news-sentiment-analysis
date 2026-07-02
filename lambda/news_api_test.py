import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&language=en"

response = requests.get(url)
data = response.json()

for article in data["results"][:10]:
    print(article["title"])