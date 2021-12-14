import json
from pprint import pprint
from datetime import datetime


def getLatestEb():
    jsonFile = "examples\ebDetails.json"
    with open(jsonFile, "r") as f:
        data = json.load(f)

    x = str(datetime.now())
    year = x.strip()[0:4]
    next_year = eval(year) + 1

    # print(len(data["Tech Department"]["Developer"]))
    # print(data["Admin Department"]["Community leader"][0]["endYear"])

    current_eb = {}
    for dept in data.keys():
        for position in data[dept].keys():
            for num in range(len(data[dept][position])):
                current_year = data[dept][position][num]["endYear"]
                if current_year == str(year) or current_year == str(next_year):
                    if dept in current_eb:
                        current_eb[dept][position] = data[dept][position]
                    else:
                        current_eb[dept] = {position: data[dept][position]}

    return current_eb


# Try to avoid sorting data -> Maintain hierarchy structure.
result = getLatestEb()
pprint(result)
