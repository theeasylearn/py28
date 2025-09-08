import math 
number = float(input("Enter any one float number"))

print(f"floor value of {number} = ",math.floor(number))
print(f"ceil value of {number} = ",math.ceil(number))
print(f"truncated value of {number} = ",math.trunc(number))
print(f"positive truncated value of {number} = ",math.fabs(math.trunc(number)))
number = int(input('enter number'))

print(f"factorial of {number} = ",math.factorial(number))
print("modulas of 10%3",math.fmod(10,3))

number = int(input('enter any one number(positive/negative)'))
print(f" positive value of {number} ",math.fabs(number))
print(f" number as negative  {number} ",math.copysign(-1,number))


