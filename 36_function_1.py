#get square using with argument with return statement
def getsquare(n):  
    square = n*n
    return square

# setdate using without argument without return statement 
def setdate():
    print('01-07-2025')
    
# get pi using without argument with return statement 
def getpi():
    pi = 3.14159
    return pi

def getdays(dayOfWeek):
    if dayOfWeek == 1:
        print("Monday")
    if dayOfWeek == 2:
        print("Tuesday")
    if dayOfWeek == 3:
        print("Wednesday")
    if dayOfWeek == 4:
        print("Thursday")
    if dayOfWeek == 5:
        print("Friday")
    if dayOfWeek == 6:
        print("Saturday")
    if dayOfWeek == 7:
        print("Sunday")
    
n= int(input("Enter the number "))
x = getsquare(n)
print(x)

setdate()

p = getpi()
print("value of pi is ",p)

d =int(input("enter the day number"))
getdays(d)

