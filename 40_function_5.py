def cal(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

a =int(input("Enter the value of a "))
b =int(input("Enter the value of b "))

r = cal(b=b,a=a)
print(r)

def division(a,b):
    reminder = a%b
    divident = a/b
    return divident,reminder

a =int(input("Enter the value of a "))
b =int(input("Enter the value of b "))

r = division(b,a)
print(r)