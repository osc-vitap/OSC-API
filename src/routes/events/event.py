import os
from flask import Blueprint, Flask, jsonify, request, abort
from src.routes.events.db_connection import connection
from src.utils.discord_webhook import send_discord_announcement

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


@event_bp.route("/announcement", methods=["GET"])
def make_announcement():
    API_KEY = os.getenv("API_KEY")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")

    api_key, event_id = request.args.get("key"), request.args.get("id")
    required_event = None

    if not (api_key == API_KEY) or not API_KEY:
        return "Unauthorized: Invalid API Key", 401

    if not WEBHOOK_URL:
        return (
            "Internal Error: No Webhook URL is configured in environment variables",
            500,
        )

    data = connection()
    print(event_id)
    if not event_id:
        required_event = data[-1]

    for event in data:
        if event_id == str(event["id"]):
            required_event = event
            break

    status = send_discord_announcement(WEBHOOK_URL, required_event)
    return jsonify({"success": status})
