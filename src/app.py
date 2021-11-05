from flask.templating import render_template
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from src.connection import connection
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "../assets"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.errorhandler(404)
def page_not_found(e):
    return "ERROR 404: CANNOT GET {}".format(request.path)


@app.route("/", methods=["GET"])
def index():
    return "Hey! This is the OSC API that is used to serve OSC details for it's various platforms."


@app.route("/event", methods=["GET"])
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
    latest = data[-1]
    return latest
