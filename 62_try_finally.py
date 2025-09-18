a=0
try:
    age = int(input("Enter the your age when you join work"))
    if age<18 or age>60:
        print("You are not allowed to work")
        raise ValueError
    else:
        a = 60-age
except ValueError:
    print("invalid age")
else:
    print(f"your age is {age} you have {a} year to do work")
finally:
    print("thank you for applying")