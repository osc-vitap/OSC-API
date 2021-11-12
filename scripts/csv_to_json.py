import csv
import json
from pprint import pprint

"""
Convert CSV to JSON. 
Use this script after collecting EB member details from Google spreadsheet.
Download the spreadsheet and add it's path to line 29.
Once completed, you should get your JSON file
"""


def csv_to_json(csvFile, jsonFile):
    json_data = {}
    heirarchy_order = {
        "Admin Department": [
            "Club Coordinator",
            "Community Leader",
            "President",
            "Director",
            "Chairman",
            "Treasurer",
            "Vice President",
            "Secretary",
            "Head of public relations",
            "Track lead",
            "HR Lead",
        ],
        "Event Department": [
            "Event lead",
            "Social Media Lead",
            "Organizer",
        ],
        "Tech Department": [
            "Technical Lead",
            "Developer",
        ],
        "Design Team": [
            "Head of marketing",
            "Chief Editor",
            "Head of videography",
            "Documentation Specialist",
            "Designer",
        ],
    }
    All_positions = []
    for key, value in heirarchy_order.items():
        for i in value:
            All_positions.append(i.capitalize())

    with open(csvFile, encoding="utf-8") as f:
        csvReader = list(csv.DictReader(f))
        for position in All_positions:
            for rows in csvReader:
                key = rows["Position"].capitalize()
                if position in key:
                    if key in json_data:
                        json_data[key].append(rows)
                    else:
                        json_data[key] = [rows]

    for key in json_data.keys():
        for i in range(len(json_data[key])):
            del json_data[key][i]["Position"]

    with open(jsonFile, "w", encoding="utf-8") as f:
        f.write(json.dumps(json_data, indent=4, separators=(",", ": ")))


if __name__ == "__main__":
    csv_to_json(csvFile="examples/ebDetails.csv", jsonFile="examples/ebDetails.json")
