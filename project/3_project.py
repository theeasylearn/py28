import mysql
import connection as con 
total = 0
# //create function to display product
def displayProduct():
    try:
        sql = "select * from product where is_deleted=0 order by id desc"
        table = con.fetch(sql)
        # print(table)
        header = f"{'ID':<5} {'Name':<48} {'Price':>8} {'Stock':>8} {'Weight':>10} {'Size':<10}"
        print(header)
        print("-"*100)
        for row in table:
            output = f"{row['id']:<5} {row['name']:<48} {row['price']:>8.2f} {row['stock']:>8} {row['weight']:>10.2f} {row['size']:<10}"
            print(output)
    except mysql.connector.errors.ProgrammingError:
        print("oops something went wrong, contact developer")
# function to take product detail as input
def displayBillItem():
    global total
    sql = "select i.id 'itemID',name,p.price 'price',qty,weight,size from product p, item i where  p.id=productid and billid=0"
    table = con.fetch(sql)
    header = f"{'itemID':<5} {'Name':<48} {'Price':>8} {'qty':>8} {'weight':>10} {'Size':<10}"
    print(header)
    print("-"*100)
    for row in table:
        output = f"{row['itemID']:<5} {row['name']:<48} {row['price']:>8.2f} {row['qty']:>8} {row['weight']:>10.2f} {row['size']:<10}"
        print(output)
        total= total + (row['price'] * row['qty'])
    print("-"*100)
    print(f"total = {total}")
def getInput():
    name = input("Enter product name ")
    price = float(input("Enter product price "))
    stock = int(input("Enter product stock "))
    description = input("Enter product description ")
    weight = float(input("Enter product weight "))
    size = input("Enter product size ")
    return name,price,stock,description,weight,size

while True:
    print("Press 1 for Bill management")
    print("Press 2 for Product management")
    print("Press 0 to Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        while True:
            print("press 1 to view items added into unsaved bill")
            print("press 2 to add new item into bill ")
            print("Press 3 to generate final bill")
            print("press 4 to delete existing bill ")
            print("press 0 to return to main menu ")
            bill_choice = int(input("Enter your choice"))
            if bill_choice == 1:
                displayBillItem()
            elif bill_choice == 2:
                displayProduct()
                # accept productid and check is this product exists or not 
                # if product does not exist display message invalid product id

                # otherwise accept qty from user and then check stock is greater then qty 
                # then insert row into item table, do not accept price from user 
                productid = int(input("Enter product id"));
                sql = "select price, stock from product where id =%s"
                data = [productid]
                table = con.fetch(sql,data)
                length = len(table)
                if length==0:
                    print("Product not found")
                else:
                    stock = table[0]['stock']
                    price = table[0]['price']
                    print("Product found...")
                    quantity = int(input("Enter quantity"))
                    if quantity>stock:
                        print(f"not enought stock, available stock = {stock}")
                    else:
                        print("Sufficient stock")
                        sql = "insert into item (productid,qty,price) values (%s,%s,%s)"
                        data = [productid,quantity,price]
                        con.run(sql,data,'Item added into bill')
            elif bill_choice == 3:
                print("you are going to save & print bill. saved bill can not be edited later on ")
                confirm =  input("Are you sure (enter yes to confirm")
                if confirm =='yes':
                    '''
                    display shop owner how much Rs he has to collect from user 
                    accept fullname, mobile and payment mode
                    insert a new rom into bill table
                    fetch last inserted row id of bill table
                    reduce stock of each row in product table by quantity of the product in 
                    update all the rows in item table where billid = 0 set billid = iast inserted row id.
                    '''
                    fullname = input("Enter customer name")
                    mobile = input("Enter mobile no")
                    mode = input("Enter payment mode (Cash/Card/UPI)")
                    sql = "INSERT INTO bill(fullname, mobile, amount, mode) VALUES (%s,%s,%s,%s)"
                    data = [fullname,mobile,total,mode]
                    con.run(sql,data,"bill generated successfully")
            elif bill_choice == 4:
                displayBillItem()
                itemID = int(input("Enter item id to delete item from bill"))
                sql = "select id from item where id=%s"
                data = [itemID]
                table = con.fetch(sql,data)
                if len(table) == 0:
                    print("Item not found")
                else:
                    sql = "delete from item where id=%s"
                    data = [itemID]
                    con.run(sql,data,"item has been removed from unsaved bill")
            elif bill_choice == 0:
                print("return to main menu")
                break # stop inner loop
            else:
                print("invalid choice")

    elif choice == 2:
        while True:
            print("press 1 to view product ")
            print("press 2 to edit product ")
            print("press 3 to add new product ")
            print("press 4 to delete existing product ")
            print("press 0 to return to main menu ")
            product_choice = int(input("Enter your choice"))
            if product_choice == 1:
                displayProduct()
            elif product_choice == 2:
                displayProduct()
                id = int(input("Enter Product id to edit product"))
                values = getInput()
                sql = "update product set name=%s,price=%s,stock=%s,description=%s,weight=%s,size=%s where id=%s"
                data = [values[0],values[1],values[2],values[3],values[4],values[5],id]
                con.run(sql,data,"product has been updated...");
            elif product_choice == 3:
                values = getInput()
                sql = "insert into product (name,price,stock,description, weight,size) values (%s,%s,%s,%s,%s,%s)"
                # data = [name,price,stock,description,weight,size]
                data = [values[0],values[1],values[2],values[3],values[4],values[5]]
                con.run(sql,data,"Product added")
            elif product_choice == 4:
                displayProduct()
                id = int(input("Enter Product id to delete product"))
            elif product_choice == 0:
                print("return to main menu")
                break # stop inner loop
            else:
                print("invalid choice")    
    elif choice == 0:
        print("Thank your for your software application")
        break #stop loop
    else:
        print("invalid choice")
