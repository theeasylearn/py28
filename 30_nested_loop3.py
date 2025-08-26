'''
    *
   **
  ***
 ****
*****
'''
line = 5
while line>=1:
    space = 1
    while space<line:
        print(' ',end=' ')
        space+=1 
    astrik = 1
    while astrik<=6-line:
        print('*',end=' ')
        astrik+=1
    print('')
    line-=1
