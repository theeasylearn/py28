#fetch all books from table 
import connection as con 
command = con.database.cursor(dictionary=True)
sql = "select * from book"
command.execute(sql)
#fetch one row 
# {'id':1,'title':'the lean startup','author':'ankit patel',price:2000}
# single_row = command.fetchone() #fetch one row as dictionary
# print(single_row)
table = command.fetchall() #fetch all rows as 2d list 
# print(table)
output =  f"{'id'}{'':10}{'title':48}{'author':24}{'price':10}"
print(output)
print("-"*95)
for row in table:
    output =  f"{row['id']}{'':10}{row['title']:48}{row['author']:24}{row['price']:10}"
    print(output)
