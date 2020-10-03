import pymysql

test = pymysql.connect(
    user='root',
    password='root1234',
    host='127.0.0.1',
    db='test',
    charset='utf8',
    port=3307,
    local_infile = 1
)

cursor = test.cursor(pymysql.cursors.DictCursor)

sql = "LOAD DATA LOCAL INFILE '/Users/eunzy/github/Transfer_data/test.csv' INTO TABLE test.test FIELDS TERMINATED BY ','; "
cursor.execute(sql)

test.commit()



