from flask import Blueprint
from src.routes.events import event

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(event.event_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    return "OSC API CONNECTION BASE"
