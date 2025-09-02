# (x+y)**2 = x**2 + 2*X*y +y**2
def nsquare(x=0,y=0):
    seq = x*x + 2*x*y + y**2
    return seq

x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))

print("both arg is given",nsquare(x,y))
print("x=2",nsquare(x=x))
print ("y=3",nsquare(y=3))





