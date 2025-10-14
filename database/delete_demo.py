import connection as con 
#create cursor 
command = con.database.cursor()
#create sql variable 
sql = "delete from book where id = %s"
#accept input 
id = int(input("Enter book id"))

#create list 
data = [id]
#run sql command 
command.execute(sql,data)
con.database.commit()
print(command.rowcount, " book deleted")
