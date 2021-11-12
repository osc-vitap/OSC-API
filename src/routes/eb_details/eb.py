from flask import Flask, jsonify, request, Blueprint
from src.routes.eb_details.db_connection import connection
from flask_pymongo import PyMongo

eb_bp = Blueprint("eb", __name__, url_prefix="/eb")


@eb_bp.route("/", methods=["GET"])
def get_data():
    data = connection()
    return "WORKING ON IT"


@eb_bp.route("/current", methods=["GET"])
def current_eb():
    data = connection()
    return "WORKING ON IT"


@eb_bp.route("/uploadCSV", methods=["POST"])
def post_data():
    pass
