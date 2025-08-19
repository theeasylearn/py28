'''
    write a program to accept 2 products price and weight from user. then findout price per gram of both product and display which is cheaper product to buy.

    steps 
    1) accept 1st product price and weight from user
    2) accept 2nd product price and weight from user 
    3) findout & display 1st product price per gram and store it into ppg1
    4) findout & display 2nd product price per gram and store it into ppg2
    5) if ppg1<ppg2 then display 1st product cheaper
    6) otherwise display 2nd product is cheaper
'''
first_product_price = int(input("Enter 1st product's price"))
first_product_weight = int(input("Enter 1st product's weight(gram)"))

second_product_price = int(input("Enter 2nd product's price"))
second_product_weight = int(input("Enter 2nd product's weight(gram)"))

ppg1 = first_product_price / first_product_weight
ppg2 = second_product_price / second_product_weight

print("first product price per gram ",ppg1)
print("second product price per gram ",ppg2)

if ppg1<ppg2:
    print("first product is cheaper")
else:
    print("second product is cheapter")


