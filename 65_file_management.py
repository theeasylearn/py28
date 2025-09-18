# write a menu driven program to copy file, rename file, delete file 
# step 1 create menu 
import os 
print("Press 1 to copy binary file")
print("Press 2 to rename file")
print("Press 3 to delete file")
choice = int(input("enter your choice"))
if choice==1:
    print('copy binary file')
    old_file = input("enter binary file name")
    new_file = input("enter new file name")
    with open(old_file,'rb') as source:
        with open(new_file,'wb') as destination:
            destination.write(source.read())
            print(f'{new_file} has been generated successfully')
elif choice==2:
    print('rename file')
    old_file = input("enter existing file name")
    new_file = input("enter new file name")
    os.rename(old_file,new_file)
    print('file renamed successfully')
elif choice==3:
    print("delete file")
    old_file = input("enter existing file name to delete file")
    os.remove(old_file)
    print('file has been removed successfully')
else:
    print("invalid choice")
    