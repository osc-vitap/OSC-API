from flask import Blueprint
from src.routes.events import event

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(event.event_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    content = """
    <h1>OSC-API</h1>
    <h2>/api/events:</h2>
    <p>
        <ul>
            <li><b>/api/event/</b>: GET complete data on all the events. </li>
            <li><b>/api/event/<int:id></b>: GET data from a particular event (from Event ID).</li>
            <li><b>/api/event/latest</b>: GET data of the latest OSC event.</li>
        </ul>
    </p>
    """
    return content
