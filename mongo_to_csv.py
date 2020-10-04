#mongo_to_csv.py

from Connection_Mongodb import get_data
from TO_CSV import savecsv

# mongodb 접속 후 딕셔너리에 list 형식으로 값을 반환받아서
# 반환받은걸 savecsv로 넘겨줘서 .csv파일로 저장함.
def mongo_to_csv():
    data_list = get_data()
    print(data_list)

    savecsv(data_list)

if __name__ =="__main__":
    mongo_to_csv()