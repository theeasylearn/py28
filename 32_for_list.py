l1 =['apple','banana','kiwi','orange']

for i in l1:
    print(i)


for i in range(5):
    print(i,end=" ")
print(" ")


for i in range(21,90):
    if i%2 !=0:
        print(i,end=' ')
print()

for i in range(21,90,5):
    print(i,end=" ")
print()

for i in range(6,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print( )

