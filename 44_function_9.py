'''
    write a program to convert given digital number into binary number system 
    steps 
    1   create variable number, remainder
    2   accept input from user  (8)
    3   divide number by 2 and get remainder 
        remainder = number % 2 
    4    print remainder 
    5   number(4) = number // 2 
    
    6   remainder(0) = number % 2
    7   print remainder 
    8    number(2) = number // 2  
    
    9   remainder(0) = number % 2 
    10  print remainder 
    11   number(1) = number // 2 
    12  remainder(1) = number % 2 
    13  print remainder
0 0 0 1 
'''
#create function 
def getBinary(number):
    if number>0:
        remainder = number % 2
        number = number // 2
        getBinary(number)
        print(remainder,end=' ')
        
number = remainder = 0
number = int(input("Enter number"))
getBinary(number) #8