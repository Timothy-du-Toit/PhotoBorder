# Focus of this application is to add a border around an image
# 1 - Application should allow for dimension selection (eg: 3:4), and after that is added, the width of the smallest border
# eg: say image is 400x300 pixels, and the selected ratio is 1:1, and pixels is 300px, final image should be 
# 400x400(+100) with an additional 300px --> 700x700 (400(+300)x300(+400))
# Process:
# - Select biggest dimension - max_dim
# - max_dim+pixel_addition
# - set other dimension to the resul
# - done
from PIL import Image
import os

def ResizeImage(fileName, pixelAddition):
    raw_image = Image.open("unprocessed_images/{}".format(fileName))
    raw_image_size = raw_image.size
    largest_dimension = max(raw_image_size)
    updated_largest_dimension = largest_dimension + pixelAddition*2

    new_size = (updated_largest_dimension, updated_largest_dimension)

    resized_image = Image.new("RGB", new_size, color="white")
    box = tuple((n - o) // 2 for n, o in zip(new_size, raw_image_size))
    resized_image.paste(raw_image, box)
    return resized_image

def CollectImageFileNames():
    files = os.listdir("unprocessed_images")
    return files


addition_input = input("Enter the number of pixels to add on the widest dimension \n")
pixel_addition = 0 if addition_input == "" else int(addition_input)
print("The output ratio will be 1:1 (square) with border width {}".format(pixel_addition))
fileNames = CollectImageFileNames()

resized_images = {}

for file in fileNames:
    resized_image = ResizeImage(file, pixel_addition)
    resized_images[file] = resized_image
    resized_image.save("processed_images/{}".format(file))
    
print("Resizing Completed for files\n{}".format(fileNames))
    