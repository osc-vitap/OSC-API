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
    data = connection("eventID", id)
    if data:
        return jsonify(data)
    else:
        return "ERROR 404: CANNOT GET {}".format(request.path)


@event_bp.route("/latest", methods=["GET"])
def latest_event():
    data = connection("latest")
    return jsonify(data)


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

    if not event_id:
        required_event = connection("latest")
    else:
        required_event = connection("eventID", event_id)

    status = send_discord_announcement(WEBHOOK_URL, required_event)
    return jsonify({"success": status})
