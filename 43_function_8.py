# finding Factorial
def factorial(n):
    if n == 0:
        print("invalid input")
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number for finding Factorial"))
output = factorial(n)
print("Factorial of", n, "is", output)