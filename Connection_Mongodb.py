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


        for i in doc:
            print("이름 : "+ i["name"])
        client.close()

    except Error as e:
        print(e)
    

if __name__ == "__main__":
    conn_mongo()