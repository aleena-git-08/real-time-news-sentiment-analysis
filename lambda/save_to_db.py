import requests
import psycopg2
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()