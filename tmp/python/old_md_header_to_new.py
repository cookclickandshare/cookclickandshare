import os
import yaml
import re

files_in_directory = os.listdir('posts/')

for every_file in files_in_directory:

    #print "Working on File :" + every_file

    f = open('posts/' + every_file, 'r')
    lines = f.readlines()
    f.close()
    lines.pop(1)
    lines.pop(3)

    relines[2]
    print lines[0:6]

    break

    # for item in range(0,7):
    #     line_append = lines[item]
    #     print line_append
