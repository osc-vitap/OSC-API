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
    collection.insert_one(data)
    return {"status": "success"}


def getData():
    collection = connection()
    data = collection.find_one(sort=[("_id", pymongo.DESCENDING)])
    data = json.loads(json_util.dumps(data))
    return data


def getCurrentEB():
    data = getData()
    return data
