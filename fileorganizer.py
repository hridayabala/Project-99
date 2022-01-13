import os
import shutil
path = input('Enter the path name to be sorted : ')
listoffiles = os.listdir(path)

for file in listoffiles:
    name,extension = os.path.splitext(file)
    extension = extension[1:]

    if extension == '' :
        continue

    if os.path.exists(path + '/'  + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)






        