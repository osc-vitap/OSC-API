from flask import Flask, jsonify, request
from dotenv import load_dotenv
from src.connection import connection
import psycopg2
import os

load_dotenv()
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
data = connection(conn)
conn.close()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hey! This is the OSC API that is used to serve event details."

@app.route("/api/", methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/api/<int:id>", methods=["GET"])
def get_id(id):
    for event in data:
        if event["id"] == id:
            return event

@app.route("/api/latest", methods=["GET"])
def latest_event():
	max = data[0]["id"]
	for event in data:
		if(event["id"] > max):
			max = event["id"]
			latest = event
	return latest


@app.route("/api/", methods=["POST"])
def post():
    content = request.get_json(force=True)
    return "Data Added Successfully"