# insert_mongodb.py

from pymongo import MongoClient
from Connection_Mongodb import conn_mongo

def insert_mongodb():
    db = conn_mongo()
    collection = db.get_collection('test')

    dict_data = [{'name': 'eunzy', 'age': 28},
                 {'name': 'Linegames', 'age': 29},
                 {'name': 'test', 'age': 30},
                 {'name': 'hope', 'age': 31},
                 {'name': 'pass', 'age': 32},
                 {'name': 'Goodluck..!', 'age': 33}]

    for i in dict_data:
        collection.insert_one(i)

if __name__ == "__main__":
    insert_mongodb()