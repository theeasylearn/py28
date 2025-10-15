import connection as con 
#example of update 
command = con.database.cursor()
sql = "update book set title=%s,author=%s,price=%s where id=%s"
title = input("Enter book title")
author = input("Enter author")
price = int(input("Enter price "))
id = int(input("Enter book id"))
data = [title,author,price,id]
command.execute(sql,data)
con.database.commit()
print(command.rowcount, " rows updated")