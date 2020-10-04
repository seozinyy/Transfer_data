# insert_data_to_mongodb.py

from pymongo import MongoClient
from Connection_Mongodb import conn_mongo

def insert_mongodb():
    db = conn_mongo()
    collection = db.get_collection('test')

    dict_data = [{'name': 'hello everyone', 'age': 28},
                 {'name': 'i am eunzy', 'age': 29},
                 {'name': 'This test', 'age': 30},
                 {'name': 'i will hope', 'age': 31},
                 {'name': 'pass', 'age': 32},
                 {'name': 'Goodluck..!', 'age': 33}]

    for i in dict_data:
        collection.insert_one(i)

if __name__ == "__main__":
    insert_mongodb()