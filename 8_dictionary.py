#concept of dictionary in python 
student = {'name':'Daksh','age':13,'weight':65.25,'gender':True}
print(student)

#we can add new key value pair 
student['email'] = 'daksha@gmail.com'
print(student)

#we can change existing value of particular key 
student['weight'] = 61.00

#we can also delete key value pair 
del student['email']

print(student)

