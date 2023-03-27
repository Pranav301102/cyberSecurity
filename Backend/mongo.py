from pymongo import MongoClient

db = None

def init():
    global db
    mongo_client = MongoClient('mongodb://127.0.0.1:27017/')
    db = mongo_client['ember-cybersecurity']
