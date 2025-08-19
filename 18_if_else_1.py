# write a program to findout whether shape is potrait or landscape using given length and width.
'''
    steps
    1) accept length from user in length variable
    2) accept width from user in width variable 
    3) if width > length then display shape is landscape
    4) otherwise display shape is potrait 
'''
length = int(input("Enter shape's length"))
width = int(input("Enter shape's width"))
if width>length:
    print("shape is landscape")
else:
    print("shape is potrait")
print('Good bye....')