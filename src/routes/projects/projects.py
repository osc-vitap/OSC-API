from flask import Blueprint, current_app, jsonify
from dotenv import load_dotenv
from src.utils.project_img import ParseOSCrepo
import requests

load_dotenv()
projects_bp = Blueprint("projects_bp", __name__, url_prefix="/projects")


def img_link(github_repolink):  # Web scraping the image link from github
    req = requests.get(f"{github_repolink}")
    parseObj = ParseOSCrepo()
    parseObj.feed(req.text)
    return parseObj.token


@projects_bp.route("/", methods=["GET"])
def project_info():
    current_app.config["JSON_SORT_KEYS"] = False
    results = []
    req = requests.get(
        "https://api.github.com/users/Open-Source-Community-VIT-AP/repos"
    )
    jsonfile = req.json()

    for i in jsonfile:  # Formatting the data
        results.append(
            {
                "Stars": i["stargazers_count"],
                "Name": i["name"],
                "Description": i["description"],
                "Image": img_link(i["html_url"]),
                "Repository_link": i["html_url"],
                "SSH": i["ssh_url"],
            }
        )

    for i in range(len(results)):  # Sorting according to stars
        for j in range(len(results) - 1):
            if results[j]["Stars"] < results[j + 1]["Stars"]:
                results[j], results[j + 1] = results[j + 1], results[j]

    for i in results:  # Removing stars from the results
        del i["Stars"]

    return jsonify(results[0:10])
