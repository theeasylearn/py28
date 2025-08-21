#write a program to findout largest number from 3 given number 
'''
    steps 
    1) accept first number and store it num1 
    2) accept second number and store it num2 
    3) accept third number and store it num3
    4) compare numbers 
        if num1  > num2 then
            if num1 > num3 then
                display num1 is largest number 
            otherwise 
                display num3 is largest number 
        else 
            if num2 > num3 then 
                display num2 is largest number 
            otherwise 
                display num3 is largest number 
    5) display good bye
''' 
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is largest number")
    else:
        print(f"{num3} is largest number")
else:
    if num2 > num3:
        print(f"{num2} is largest number")
    else:
        print(f"{num3} is largest number")

print("Good bye....")