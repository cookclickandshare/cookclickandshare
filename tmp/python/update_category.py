import os

files_in_directory = os.listdir('posts/')
for every_file in files_in_directory:


    fin = open("posts/" + every_file)
    fout = open("updated_posts/" + every_file, "wt")

    line = fin.readlines()
    if 'category' in line[5]:
        print line[5], line[5].split(':')[1].upper()
        line[5] = line[5].split(':')[0] + ': ' + str(line[5].split(':')[1].upper())

    for remain_line in line:
        fout.write(remain_line)
    fin.close()
    fout.close()

