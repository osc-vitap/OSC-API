from dotenv import load_dotenv
import psycopg2
import os

if __name__ == "__main__":
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    print("Connected successfully")