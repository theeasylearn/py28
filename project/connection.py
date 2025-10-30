import mysql.connector as connector
import mysql
try:
    database = connector.connect(host='localhost',user='root',passwd='',database='python_project',port='3306')
    print('connection created.....')
except connector.Error as e:
    print('Error occurred (please read detail given below)')
    print(e.errno)
    print(e.msg)
    
#create function that will run insert,update,delete sql command 
def run(sql,data,msg):
    try:
        #create sql command 
        #excecute sql command
        command = database.cursor() #create cursor
        command.execute(sql,data) 
        database.commit()
        print(msg)
        key = input("press any to continue....")
    except mysql.connector.errors.ProgrammingError as error:
        print("oops something went wrong, contact developer")
        print(error)
def fetch(sql):
    command = database.cursor(dictionary=True) #create cursor
    command.execute(sql)
    table = command.fetchall()
    return table