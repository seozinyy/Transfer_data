from pymongo import MongoClient
import traceback

host = 'localhost' 
port = 27017 

def conn_mongo():
    try:
        client = MongoClient(
            host = host,
            port = port
        )
        db = client.test

    except Error as e:
        print(e)

    return db

def get_data():
    db = conn_mongo()
    collection = db.test
    doc = collection.find()

    data = []

    for i in doc:
        #print("이름 : "+ i["name"])
        dict_data = { "name" : i.get("name"), "age" : i.get("age") }
        data.append(dict_data)

    return data


if __name__ == "__main__":
    data_list = get_data()
    print(data_list)