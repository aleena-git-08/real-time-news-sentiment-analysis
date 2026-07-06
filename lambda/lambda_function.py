import json
import requests
import boto3
import os

def lambda_handler(event, context):

    API_KEY = os.getenv("API_KEY")