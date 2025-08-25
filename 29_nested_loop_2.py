'''
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1
'''
row = 1
while row<=5:
    column = 5
    while column>=row:
        print(column%2,end=' ')
        column = column - 1
    print(" ")
    row = row + 1

