import random as rd 
fruits = ["Apple","Banana","Orange","Mango","Pineapple","Grapes","Strawberry","Blueberry","Watermelon","Papaya","Guava","Pomegranate","Kiwi","Lychee","Peach","Plum","Cherry","Coconut","Dragonfruit","Apricot"]
print(fruits)
print("Any one random item from fruits",rd.choice(fruits))
print("Any two random items from fruits",rd.choices(fruits,k=2))
print("Any three random items from fruits",rd.choices(fruits,k=3))
rd.shuffle(fruits)
print("after shuffle")
print(fruits)

another_list = rd.sample(fruits,k=5) #return shuffed list as another list
print(another_list)