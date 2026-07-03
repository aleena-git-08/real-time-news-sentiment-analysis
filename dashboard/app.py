import os
import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

query = "SELECT * FROM news_data"

df = pd.read_sql(query, conn)

st.title("News Sentiment Dashboard")

st.subheader("News Records")
st.dataframe(df)