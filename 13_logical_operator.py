# concept of logical operator
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

result = num1 == num2 and num2 == num3
print(f"{result} = {num1} == {num2} and {num2} == {num3}")


result = num1 < num2 or num2 < num3
print(f"{result} = {num1} < {num2} or {num2} < {num3}")

result = not (num1 == num2 and num2 == num3)
print(f"{result} = not ({num1} == {num2} and {num2} == {num3})")