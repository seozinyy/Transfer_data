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
        collection = db.test
        doc = collection.find()

        data = []

        for i in doc:
            #print("이름 : "+ i["name"])
            dict_data = { "name" : i.get("name"), "age" : i.get("age") }
            data.append(dict_data)

        client.close()

        return data

    except Error as e:
        print(e)
    

if __name__ == "__main__":
    data_list = conn_mongo()
    print(data_list)