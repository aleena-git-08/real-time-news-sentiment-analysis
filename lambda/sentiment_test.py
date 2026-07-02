import os
import requests
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

API_KEY = os.getenv("API_KEY")