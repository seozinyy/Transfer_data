# Transfer_data

# README.md
도커를 이용해서 시스템환경을 구축했습니다. 
하단의 각 단계별 작업이 정상적으로 수행되도록 구축했습니다. 세부 작업절차 및 결과물은 첨부드린 "문서" 참조부탁드립니다. 

## 작업절차
1. Docker이용 하여 Mongodb(3.6v) / Mysql(5.7v) Install
 - mongodb는 명령문으로 설치 
 - Mysql은 docker-compose로 설치 (github에 docker-compose.yml , init sql 파일첨부)
2. 작업을 위한 테스트용 계정생성(root)
3. 몽고DB에 테스트 콜렉션 생성 후 Document insert 
4. 파이썬으로 제어하기 위한 pymongo 모듈 설치 및 Python3 설치 
5. Mysql에 pymysql 설치 
6. mongodb 연결하고 데이터 insert
7. 6번의 데이터 Mysql로 Import하기 위한 test 테이블 생성 
8. mongodb의 데이터 .csv파일로 export
9. 8번의 .csv파일을 Mysql로 import
10. 각 단계가 정상적으로 수행되었는지 결과물 확인

## 파이썬 파일 설명
1. Connection_Mongodb.py
-- Mongodb 연결 & 데이터 가져오는파일
-- conn_mongo()  // DB연결 함수
-- get_data()    // 데이터 가져오는 함수 

2. TO_CSV.py
-- 딕셔너리 형태의 리스트를 csv파일 형태로 만드는 작업

3. insert_data_to_mongo.py
-- mongodb에 데이터 insert하는 프로그래밍

4. mongo_to_csv.py
-- mongodb의 데이터를 csv파일로 export 작업

5. insert_data_to_mysql.py
-- Mysql Connection & csv파일을 Mysql로 import
