from PIL import Image
import os

#
# Pick up all the images from the directory
#
files_in_directory = os.listdir('images/input_unsplash/')

# we are using the counter for the output image name.
counter = 1

# process each file.
for every_file in files_in_directory:

    inbound_image_to_process = "images/input_unsplash/" + every_file
    image_to_process = Image.open(inbound_image_to_process)

    img_width, img_height = image_to_process.size
    print img_width, img_height, float(img_width / img_height)

    # Check if the images is not already `horizontal` (width way larger than height - aka panorama).
    if float(img_width / img_height) <= 1.0:

        left = img_width / 2
        top = img_height / 2
        right = 3 * img_width / 3
        bottom = 3 * img_height / 3

        print left, top, right, bottom

        # Check if the image height is not less than what we want.
        if img_height > 1200:
            cropped_example = image_to_process.crop((0, top, right, bottom))

            # Enable to check the image
            # cropped_example.show()

        # Large Images can be cropped.
        else:
            cropped_example = image_to_process.crop((0, top, right, img_height))
            # cropped_example.show()

        # Finally save them as jpeg.
        cropped_example.save("images/output/unsplash-image-" + str(counter) + ".jpg", "JPEG")
        counter = counter + 1
