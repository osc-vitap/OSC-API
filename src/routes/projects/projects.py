from flask import Blueprint, jsonify
from dotenv import load_dotenv
import requests
from html.parser import HTMLParser

load_dotenv()
projects_bp = Blueprint("projects_bp", __name__, url_prefix="/projects")


class ParseOSCrepo(HTMLParser):  # The HTML parser for scraping img link from
    token: str = None

    def handle_starttag(self, tag: str, attrs: str):
        if self.token:
            return
        if tag != "meta":
            return
        token = None
        for (index, (i, j)) in enumerate(attrs):
            if i == "content":
                token = j
            if all([i == "property", j == "og:image"]):
                if token:
                    self.token = token
                    return
                for (inner_index, (ni, nj)) in enumerate(attrs, start=index):
                    if ni == "content":
                        self.token = nj
                        return


def imglink(github_repolink):  # Web scraping the image link from github
    req = requests.get(f"{github_repolink}")
    parseObj = ParseOSCrepo()
    parseObj.feed(req.text)
    return parseObj.token


@projects_bp.route("/", methods=["GET"])
def project_info():
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
                "Image": imglink(i["html_url"]),
                "Repository_link": i["html_url"],
                "SSH": i["ssh_url"],
            }
        )

    for i in range(len(results)):  # Sorting according to stars
        for j in range(len(results) - 1):
            if results[j]["stars"] < results[j + 1]["stars"]:
                results[j], results[j + 1] = results[j + 1], results[j]

    for i in results:  # Removing stars from the results
        del i["stars"]

    return jsonify(results[0:10])
