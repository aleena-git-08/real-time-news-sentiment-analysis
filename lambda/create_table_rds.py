import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST1"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD1"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS news_data (
    id SERIAL PRIMARY KEY,
    title TEXT,
    sentiment VARCHAR(20)
);
""")

conn.commit()

print("Table created successfully!")