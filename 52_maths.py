import math 
number = float(input("Enter any one float number")) # 7.12
print(f"Original number = {number}") 

print(f"ceil value of {number}",math.ceil(number))   #8
print(f"floor value of {number}",math.floor(number)) #7
print(f"truncated value of {number}",math.trunc(number)) # 7 
print("{number} value before and after point")
print(math.modf(number))
print(f"10 % 3 = ",math.fmod(10,3)) # 1
print(f"factorial of 6 ",math.factorial(6)) # 720

number = float(input("Enter any one integer number")) # 7.12
print(f"absolute value of {number}",math.fabs(number)) 
print(f"negative value of {number}",math.copysign(number,-1))

