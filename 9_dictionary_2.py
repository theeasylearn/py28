#dictionary methods 
dish = {'name':'Pizza','weight':300,'price':350}
print(dish)

#get only keys 
print(dish.keys())

#get only values 
print(dish.values())

#get key value pair is object
print(dish.items())

#list has keys 
keys = ['from','to','km','price','type']

#create dictionary from keys 
bus = dict.fromkeys(keys)

print(bus)

#update dictionary
bus['price'] = 1000

bus.update({'from':'bhavnagar'})
bus.update({'to':'baroda'})
bus.update({'seat':50})
print(bus)
bus.pop('price')
bus.popitem()
print(bus)
bus.clear()
print(bus)
