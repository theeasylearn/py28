'''
write a program to display following pattern 
*
* *
* * *
* * * *
* * * * *
'''

row = 1
while row<=5: #outer loop 
    count = 1
    while count<=row: #inner loop (print astrik)
        print('*',end=' ')
        count = count + 1
    print("")
    row = row + 1
