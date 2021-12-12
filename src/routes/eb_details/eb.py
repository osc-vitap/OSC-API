from flask import request, Blueprint, flash, current_app
from pymongo import results
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os

from src.routes.eb_details.db_connection import *
from src.utils.csv_to_json import csv_to_json


load_dotenv()
UPLOAD_FOLDER = "temp"
ALLOWED_EXTENSIONS = {"csv"}
eb_bp = Blueprint("eb", __name__, url_prefix="/eb")


@eb_bp.route("/", methods=["GET"])
def get_data():
    return getData()


@eb_bp.route("/current", methods=["GET"])
def current_eb():
    return getCurrentEB()


@eb_bp.route("/add_data", methods=["GET", "POST"])
def uploadFiles():
    current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if request.method == "POST":
        key, year = request.args.get("key"), int(request.args.get("year"))
        if not key == os.getenv("API_KEY"):
            return "Unauthorized: Invalid API Key", 401
        if not year:
            return (
                "Error: Please provide the year for which you want to upload EB details",
                400,
            )
        if "file" not in request.files:
            return (
                "ERROR: File not found. Please upload a CSV file containing details",
                400,
            )
        file = request.files["file"]
        filename = file.filename
        if filename == "":
            flash("No file selected")
            return "ERROR: File not found.", 400
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"csv"}
        if file and allowed_file:
            filename = secure_filename(filename)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            try:
                result = csv_to_json(f"{UPLOAD_FOLDER}/{filename}", year)
            except:
                return (
                    "ERROR: Make sure to follow exact structure as provided in examples/ebDetails.csv",
                    400,
                )
            return result
        else:
            return ("ERROR: Only CSV files are allowed", 400)
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """
