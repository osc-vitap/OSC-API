from pymongo import MongoClient
from bson import json_util
from dotenv import load_dotenv
import pymongo
import json
import os


def connection():
    load_dotenv()
    CONNECTION_STRING = os.getenv("MONGO_DB_CON")
    db = MongoClient(CONNECTION_STRING).ebDetails
    collection = db["details"]
    return collection


def addContent(data, year):
    collection = connection()
    if collection.count_documents({"Year": year}) == 0:
        collection.insert_one(data)
    else:
        collection.update_one(
            {"Year": year},
            {
                "$set": {
                    "Admin Department": data["Admin Department"],
                    "Event Department": data["Event Department"],
                    "Tech Department": data["Tech Department"],
                    "Design Team": data["Design Team"],
                }
            },
        )
    return {"status": "success"}


def deleteData(year):
    collection = connection()
    try:
        collection.delete_one({"Year": year})
        return {"status": "success", "message": "Data deleted"}
    except:
        return {"status": "fail", "message": "Year not found"}, 400


def getData(year, department):
    collection = connection()
    try:
        data = collection.find_one({"Year": year})
        del data["_id"]
        if not department == None:
            department = department.replace("-", " ")
            department = department.title()
            data = data[department]
    except:
        return False
    data = json.loads(json_util.dumps(data))
    return data


def getCurrentEB(department):
    collection = connection()
    latest = collection.find({}).sort("Year", pymongo.DESCENDING).limit(1)
    year = latest[0]["Year"]
    return getData(year, department)
