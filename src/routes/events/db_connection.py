from dotenv import load_dotenv
import psycopg2
import os
import json


def connection(type=None, *args):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    if not type:
        query = """SELECT * FROM eventreg_event"""
    elif type == "latest":
        query = """SELECT * FROM eventreg_event ORDER BY id DESC LIMIT 1"""
    elif type == "eventID":
        query = f"""SELECT * FROM eventreg_event WHERE id = {args[0]}"""
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    result = []

    for row in data:
        result.append(
            {
                "id": row[0],
                "eventName": row[1],
                "eventCaption": row[2],
                "eventDescription": row[3],
                "eventVenue": row[4],
                "eventDate": row[5],
                "eventStartTime": row[6],
                "eventEndTime": row[7],
                "eventRegEndDate": row[8],
                "eventRegEndTime": row[9],
                "eventSpeaker": row[10],
                "eventURL": row[11],
                "eventDocumentation": row[12],
                "eventLogo": "https://drive.google.com/uc?export=view&id={}".format(
                    str(row[13].split("/")[5])
                ),
            }
        )

    if not result:
        return None

    result.sort(key=lambda x: x["id"])
    json_data = json.dumps(result, indent=4, default=str)
    return json.loads(json_data)
