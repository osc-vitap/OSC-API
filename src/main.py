from dotenv import load_dotenv
from modules.connection import connection
import psycopg2
import os

if __name__ == "__main__":
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    connection(conn)