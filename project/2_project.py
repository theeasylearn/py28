import mysql
import connection as con 
while True:
    print("Press 1 for Bill management")
    print("Press 2 for Product management")
    print("Press 0 to Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        while True:
            print("press 1 to view bill ")
            print("press 2 to edit bill ")
            print("press 3 to add new bill ")
            print("press 4 to delete existing bill ")
            print("press 0 to return to main menu ")
            bill_choice = int(input("Enter your choice"))
            if bill_choice == 1:
                print("display all bills")
            elif bill_choice == 2:
                print("provide option to edit bill")
            elif bill_choice == 3:
                print("provide option to add new bill")
            elif bill_choice == 4:
                print("provide option to deleted bill")
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
                try:
                    sql = "select * from product order by id desc"
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
            elif product_choice == 2:
                print("provide option to edit product")
            elif product_choice == 3:
                name = input("Enter product name ")
                price = float(input("Enter product price "))
                stock = int(input("Enter product stock "))
                description = input("Enter product description ")
                weight = float(input("Enter product weight "))
                size = input("Enter product size ")
                sql = "insert into product1 (name,price,stock,description, weight,size) values (%s,%s,%s,%s,%s,%s)"
                data = [name,price,stock,description,weight,size]
                con.run(sql,data,"Product added")
            elif product_choice == 4:
                print("provide option to deleted product")
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
