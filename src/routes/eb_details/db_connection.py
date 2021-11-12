from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
import pymongo
import json
import os

from pymongo.message import insert
from pymongo.results import InsertManyResult


def connection():
    return "WORKING ON IT"


def addContent(data):
    load_dotenv()
    CONNECTION_STRING = os.getenv("MONGO_DB_CON")
    client = MongoClient(CONNECTION_STRING)
    db = client.ebDetails
    collection = db["details"]

    collection.insert_one(data)

    client.close()
    return "<h2>DATA UPLOADED SUCCESSFULLY</h2>"
