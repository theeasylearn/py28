def square(x,y):
    s = x*x +2*x*y +y*y
    # s = x**2 +2*x*y + y**2
    return s
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))

S = square(x,y)
print(f"value of x = {x}, y = {y}, (x+y)**2 = {S}")