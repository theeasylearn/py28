# finding Factorial
def factorial(n):
    if n==1:
        return n
    else:
        n= n*factorial(n-1)
        return n

n= int(input("Enter the number for find factorial "))
a = factorial(n)
print(f"factorial of {n} is {a}")