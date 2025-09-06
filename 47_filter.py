l1 =[1,5,9,41,45,78,91,2,65,45,61]

# a=[]
# for i in l1:
#     if i<50:
#         a.append(i)
# print(a)

a = filter(lambda l1:l1<50,l1)
print(list(a))

l1.sort()
print(l1)