import mysql.connector as connector
try:
    database = connector.connect(host='localhost',user='root',passwd='',database='py30',port='3306')
    print('connection created.....')
except connector.Error as e:
    print('Error occurred (please read detail given below)')
    print(e.errno)
    print(e.msg)
    