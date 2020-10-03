#TO_CSV.py

import csv

# csv 파일화 하는 함수
# 딕셔너리 형식의 리스트
# 딕셔너리는 .values()함수를 사용할 수 있다.
def savecsv(dict_data_list):
  with open('test.csv','w') as f:
    w = csv.writer(f)
    for dict_data in dict_data_list:
      w.writerow(dict_data.values())


# 기능이 잘 되는지 테스트용도
if __name__ == "__main__":
  d ={}
  d["name"]="eunzy"
  d["age"]=28

  savecsv([d])


