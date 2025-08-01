#concept of list in python 
list = ['Audi',100,3.14,True,None]
another_list = ['Ankit',False]
print(list)
#display 1st item 
print(list[0]) #Audi

#display two item from left 
print(list[0:2]) #Audi 100

#display 1st and 2nd item
print(list[1:3]) #100,3.14

list[0] = "BMW"
print(list)

# how to delete item 
#delete 2nd item
del list[1] 
print(list)
print(list+another_list)
print(list*3)

#how to insert new value into list
list.append('Apple')
list.append(21.22)
list.append(True)
print(list)

#how to insert value at begining
list.insert(0,"laptop")
list.insert(0,500)
print(list)
#insert at 2nd position
list.insert(1,'India')
print(list)

#delete whole list 
del another_list
# print(another_list)
#empty list 
list.clear()
print(list)