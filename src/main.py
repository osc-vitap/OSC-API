from modules.connection import connection
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import psycopg2
import os
import json

if __name__ == "__main__":
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    data = connection(conn)
    conn.close()

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def get():
        return "Hey! This is the OSC API that is used to serve event details."

    @app.route("/api/", methods=["GET"])
    def get_data():
        return data

    @app.route("/api/<int:id>", methods=["GET"])
    def get_id(id):
        for event in json.loads(data):
            if event["id"] == id:
                return event

    @app.route("/api/", methods=["POST"])
    def post():
        content = request.get_json(force=True)
        return "Data Added Successfully"

    app.run()
