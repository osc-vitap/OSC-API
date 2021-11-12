from flask import (
    Flask,
    jsonify,
    request,
    Blueprint,
    url_for,
    redirect,
    flash,
    current_app,
)
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo
import os
from src.routes.eb_details.db_connection import connection

UPLOAD_FOLDER = "File_upload"
ALLOWED_EXTENSIONS = {"csv"}
eb_bp = Blueprint("eb", __name__, url_prefix="/eb")


@eb_bp.route("/", methods=["GET"])
def get_data():
    data = connection()
    return "WORKING ON IT"


@eb_bp.route("/current", methods=["GET"])
def current_eb():
    data = connection()
    return "WORKING ON IT"


@eb_bp.route("/uploadCSV", methods=["GET", "POST"])
def uploadFiles():
    current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if request.method == "POST":
        if "file" not in request.files:
            return "<h2> ERROR: File not found. Please upload a CSV file containing details </h2>"
        file = request.files["file"]
        filename = file.filename
        if filename == "":
            flash("No selected file")
            return "<h2> ERROR: File not found. Please upload a CSV file containing EB details </h2>"
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"csv"}
        if file and allowed_file:
            filename = secure_filename(filename)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            return "<h3>File uploaded successfully!<h3>"
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """
