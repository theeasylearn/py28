# lambda function
getsqure = lambda n : n*n
getarea = lambda getsqure:3.14*getsqure**2


n = int(input("Enter the number"))
print(getsqure(n))
print(getarea(n))