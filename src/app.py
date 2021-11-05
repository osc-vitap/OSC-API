from flask.templating import render_template
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from src.connection import connection
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
api_cors_config = {
  "origins": ["http://localhost:3000"]
}
CORS(app, resources={"/*": api_cors_config})


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
    temp = 0
    for event in data:
        if event["id"] == id:
            temp = 1
            break
        else:
            temp = 0
    if temp == 1:
        event = jsonify(event)
        return event
    else:
        return "ERROR 404: CANNOT GET {}".format(request.path)


@app.route("/event/latest", methods=["GET"])
def latest_event():
    data = connection()
    latest = data[-1]
    return latest
