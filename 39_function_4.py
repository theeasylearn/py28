def getMerit(math,science,english,computer,history,drawing):
    print(math,science,english,computer,history,drawing)
    total = math + science + english
    return	total

maths =90
science = 80
english = 85
computer = 95
history = 70
drawing = 85

# m = getMerit(drawing,science,english,maths,history,computer)
x = (getMerit(computer=computer,history=history,drawing=drawing, math=maths,science=science,english=english))
print(f"maths = {maths}, s = {science},e= {english}, c = {computer}, h = {history}, d = {drawing} rank = {x}")