from pymongo import MongoClient, InsertOne, collection
from bson import json_util
from dotenv import load_dotenv
import pymongo
import json
import os

from pymongo.message import insert
from pymongo.results import InsertManyResult


def connection():
    load_dotenv()
    CONNECTION_STRING = os.getenv("MONGO_DB_CON")
    db = MongoClient(CONNECTION_STRING).ebDetails
    collection = db["details"]
    return collection


def addContent(data):
    collection = connection()
    collection.insert_one(data)
    return "<h2>DATA UPLOADED SUCCESSFULLY</h2>"


def getData():
    collection = connection()
    data = collection.find_one()
    data = json.loads(json_util.dumps(data))
    return data
