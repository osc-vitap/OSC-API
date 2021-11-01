from modules.connection import connection
from dotenv import load_dotenv
from flask import Flask, jsonify
import psycopg2
import os

if __name__ == "__main__":
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    data = connection(conn)
    conn.close()

    app = Flask(__name__)

    @app.route('/')
    def get():
        return "Hey! This is the OSC API that is used to serve event details."

    @app.route('/api/')
    def get_data():
        return data

    @app.route('/api/<int:id>')
    def get_id(id):
        return data[str(id)]

    app.run()