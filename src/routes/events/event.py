from flask import Flask, jsonify, request, Blueprint
from src.routes.events.db_connection import connection

event_bp = Blueprint("events", __name__, url_prefix="/event")


@event_bp.route("/", methods=["GET"])
def get_data():
    data = connection()
    return jsonify(data)


@event_bp.route("/<int:id>", methods=["GET"])
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


@event_bp.route("/latest", methods=["GET"])
def latest_event():
    data = connection()
    latest = data[-1]
    return latest
