import connection as con 
#create cursor 
command = con.database.cursor()
#create sql variable 
sql = "insert into book (title,author,price) values (%s,%s,%s)"
#accept input 
title = input("Enter book title")
author = input("Enter author name")
price = int(input("Enter book price"))

#create list 
data = [title,author,price]
#run sql command 
command.execute(sql,data)
con.database.commit()
print(command.rowcount, " new book inserted")
