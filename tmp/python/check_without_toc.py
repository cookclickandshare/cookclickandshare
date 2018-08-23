import os

files_in_directory = os.listdir('posts/')
for every_file in files_in_directory:


    fin = open("posts/" + every_file)

    line = fin.readlines()

    if 'false' in line[1]:
        print every_file
        print line[1], line[4]

    fin.close()

