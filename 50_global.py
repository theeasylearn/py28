amount = int(input("Enter the amount"))

def addamount():
    global amount
    a=10    #local variable
    print(f"amount before add is ={amount}")
    amount = amount + a
    print(f"amount after add is ={amount}")

addamount()