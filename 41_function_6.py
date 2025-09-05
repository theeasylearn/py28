# create function that has any number of arguments (Arbitrary Argument)
# we can call such function with 1,2,3 or more arguments 
def getMax(*numbers):
    max = numbers[0] # 100
    for num in numbers:
        if max<num:
            max = num 
    return max 
max = getMax(100,50,80,200,125,1000,-50,5000,4500,1250)
print(max)
