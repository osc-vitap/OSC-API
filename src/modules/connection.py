import json
from pprint import pprint


def connection(conn):
    cursor = conn.cursor()
    query = """SELECT * FROM eventreg_event"""
    cursor.execute(query)
    data = cursor.fetchall()

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
                "eventLogo": row[13],
            }
        )

    json_data = json.dumps(result, indent=4, default=str)
    return json.loads(json_data)