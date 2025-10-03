from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

def connect_db():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    uri = os.getenv("DB_URI")
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

def get_collection(db_name, collection_name):
    client = connect_db()
    db = client[db_name]
    collection = db[collection_name]
    return collection

print(get_collection("cluster0", "users"))