import os

# Replace with the folder path you want to check
folder_path = 'images'

# Get a list of all files in the folder
files = os.listdir(folder_path)
for file in files:
    print(file)
    try:
        with open('images/' + file,'rb') as source:
            with open('images_2/' + file,'wb') as destination:
                destination.write(source.read())
                print(f'{file} has been copied')
    except PermissionError:
        print('it is not file, may be folder so it is skipped')
