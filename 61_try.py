a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

try:
    x=a/b
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("value of b can not be a zero")

else:
    print(f"value of a is {a} value of b is {b} division of a/b is {x}")