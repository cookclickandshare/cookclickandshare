import os

files_in_directory = os.listdir('../../_posts/')
counter = 0
for every_file in files_in_directory:


    fin = open("../../_posts/" + every_file)
    fout = open("updated_posts/" + every_file, "wt")

    line = fin.readlines()


    #header: { overlay_image: /assets/images/unsplash-image-1.jpg, og_image: /assets/images/page-header-og-image.png, caption: "Photo credit: [**Unsplash**](https://unsplash.com)" }

    if 'header' in line[7] or 'header' in line[8]:
        print "Do no Change"

    elif '---' in line[7]:
        print line[7]
        if counter == 5:
            counter = counter + 2
        else:
            counter = counter + 1
        line[7] = "header: { overlay_image: /assets/images/unsplash-image-"+ str(counter) +".jpg, og_image: /assets/images/page-header-og-image.png, caption: 'Photo credit: [**Unsplash**](https://unsplash.com)' }" + "\n" + "---\n"
        if counter == 11:
            counter = 0

    elif '---' in line[8]:
        print line[8]
        if counter == 5:
            counter = counter + 2
        else:
            counter = counter + 1
        line[8] = "header: { overlay_image: /assets/images/unsplash-image-"+ str(counter) +".jpg, og_image: /assets/images/page-header-og-image.png, caption: 'Photo credit: [**Unsplash**](https://unsplash.com)' }" + "\n" + "---\n"
        if counter == 11:
            counter = 0

    for remain_line in line:
        fout.write(remain_line)
    fin.close()
    fout.close()

    break