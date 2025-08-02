#list related methods 
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry','apple']
grains = ['wheat', 'rice', 'barley', 'oats', 'corn', 'millet', 'rye']
print(fruits,grains)

#extend fruits, by adding all items from grains
fruits.extend(grains)
print(fruits)

#remove item by name 
fruits.remove('date')

#remove item by position
fruits.pop(1)

print(fruits)

#count no of items (apple)
print(fruits.count('apple'))

#get item at 1st position
# print(fruits[50]) #will return error

# print(fruits.index(50)) #value error will be raised 
fruits.sort()
print(fruits)

#descending order
fruits.reverse()
print(fruits)

# copy_of_fruits = fruits wrong way of creating copy 
copy_of_fruits = fruits.copy()

print(copy_of_fruits)
copy_of_fruits.clear()
print(fruits,copy_of_fruits)