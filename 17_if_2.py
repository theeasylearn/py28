#write a program to convert 24 hours format time given by user into 12 hours format time 
'''
    input : hours 15 output 3 PM 
    input : hours 21 output 9 PM 
    input : hours 08 output 8 AM 

    steps 
    -----------------------------------------------
    1) accept hours from user in hours variable
    2) if hours == 0 then print 12 with midnight 
    3) if hours == 12 then print hours with noon 
    5) if hours<12 then print hours with AM 
    5) if hours>12 then 
        subtract 12 from hours 
        print hours with PM 
'''
hours = int(input("Enter hours"))
if hours == 0:
    print('12 o clock midnight')
if hours == 12:
    print('12 0 clock noon')
if hours<12 and hours !=0:
    print(hours,' AM')
if hours>12:
    hours = hours - 12 
    print(hours,' PM')
print('Good bye')

