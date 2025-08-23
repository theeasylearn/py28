# write a program to findout factorial of given number 
'''
    input : 5 process : 5 x 4 x 3 x 2 x 1 output = 120
    input : 3 process : 3 x 2 x 1 output = 6
'''
number = int(input("Enter number")) # 4
factorial = number #4
multiplier = number - 1 # 3

while multiplier>=1:
    factorial = factorial * multiplier #12 #wrong
    multiplier=multiplier - 1 # 2

print(factorial)



