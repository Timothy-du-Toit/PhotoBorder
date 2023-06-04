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
    