#write a program to read file 
try:
    filename = input("Enter file name (file must exist in same folder)")
    mode = 'r' #r = read mode (only file read operation is possible)
    #open file 
    file = open(filename,mode)
    #fetch each line and display it 
    count = 0
    # we use foreach loop to display data in file object
    for line in file:
        print(line,end='')
        count=count+1
    print()
    print(f"count = {count}")
    file.close()
except FileNotFoundError:
    print("file does not exists")
except PermissionError:
    print("it is not file. you might not have permission to access this file")
except UnicodeDecodeError:
    print("it is not text file. might be binary file")
finally:
    print('thank you for using our program')