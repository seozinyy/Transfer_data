from Connection_Mongodb import conn_mongo
from TO_CSV import savecsv

def mongo_to_csv():
    data_list = conn_mongo()
    print(data_list)

    savecsv(data_list)

if __name__ =="__main__":
    mongo_to_csv()