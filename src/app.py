from flask.templating import render_template
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_from_directory
import os
from src.routes import api_blueprint


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    api_cors_config = {
        "origins": [
            "/*",
            "http://localhost:3000",
            "https://www.oscvitap.org/events",
        ]
    }
    CORS(app, resources={"/*": api_cors_config})
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    @app.route("/", methods=["GET"])
    def index():
        return "<h3>Hey! This is the OSC API that is used to serve OSC details for it's various platforms.<h3>"

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "../assets"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    app.register_blueprint(api_blueprint)

    return app
