# write a program to make sum of all digits in given number
'''
    input: 12345 output: 1+2+3+4+5  output = 15
'''
number = int(input("Enter number")) #12345
sum = 0 
while number>0:
    remainder = number % 10 #5
    sum = sum + remainder
    number = number // 10 #1234
print(sum)