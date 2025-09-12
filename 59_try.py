try:
    number = int(input("Enter the number to find qube "))
    if number<0:
        print("number is negative")
        number = 0-number

    qube = number**3
    print(f"qube of {number}={qube}")
except ValueError:
    print("Invalid input only int number allowed")
