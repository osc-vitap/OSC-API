import csv
import json
from src.routes.eb_details.db_connection import *


def csv_to_json(csvFile):
    json_data = {}
    position_data = {}
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
                    if key in position_data:
                        position_data[key].append(rows)
                    else:
                        position_data[key] = [rows]

    for key in json_data.keys():
        for i in range(len(json_data[key])):
            del json_data[key][i]["Position"]

    dept_list = heirarchy_order.keys()
    for dept in dept_list:
        json_data[dept] = {}
        for position, value in position_data.items():
            for i in range(len(heirarchy_order[dept])):
                if position in heirarchy_order[dept][i].capitalize():
                    if dept in json_data:
                        json_data[dept][position] = value

    # jsonFile = "temp/temp_json_file.json"
    # with open(jsonFile, "w", encoding="utf-8") as f:
    #     f.write(json.dumps(json_data, indent=4, separators=(",", ": ")))
    os.remove(csvFile)
    return addContent(json_data)
