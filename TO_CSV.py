#export_mongo36_data.py

import csv

# csv 파일화 하는 함수
def savecsv(dict_data):
  with open('test.csv','w') as f:
    w = csv.writer(f)
    w.writerow(dict_data.values())

if __name__ == "__main__":
  d ={}
  d["name"]="eunzy"
  d["age"]=28

  savecsv(d)


