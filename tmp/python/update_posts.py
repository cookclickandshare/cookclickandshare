import os

files_in_directory = os.listdir('posts/')
for every_file in files_in_directory:


    fin = open("posts/" + every_file)
    fout = open("updated_posts/" + every_file, "wt")

    line = fin.readlines()

    line.pop(1)
    line.pop(3)

    line[0] = "---\n" + "toc: true \ntoc_label: 'Contents' \ntoc_icon: 'cog'\n"
    line[2] = line[2].split(':')[0] + ': ' + str(line[2].split(':')[1].title().split()) + '\n'
    line[3] = line[3].split(':')[0] + ': ' + str(line[3].split(':')[1].lower().split()) + '\n'

    for remain_line in line:
        fout.write(remain_line)
    fin.close()
    fout.close()