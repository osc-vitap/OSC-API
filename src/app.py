from flask import Flask, jsonify, request
from src.connection import connection


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hey! This is the OSC API that is used to serve OSC details for it's various platforms."

@app.route("/event/", methods=["GET"])
def get_data():
	data = connection()
	return jsonify(data)

@app.route("/event/<int:id>", methods=["GET"])
def get_id(id):
	data = connection()
	for event in data:
		if event["id"] == id:
		    return event

@app.route("/event/latest", methods=["GET"])
def latest_event():
	data = connection()
	max = data[0]["id"]
	i = 0
	for event in data:
		if(event["id"] > max):
			max = event["id"]
			i = i + 1
	latest = data[i]
	return latest