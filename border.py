from PIL import Image
import os
OUTPUT_FOLDER = "processed_images"


def ResizeImage(inputPath, fileName, pixelAddition):
    raw_image = Image.open("{}/{}".format(inputPath, fileName))
    raw_image_size = raw_image.size
    largest_dimension = max(raw_image_size)
    updated_largest_dimension = largest_dimension + pixelAddition*2

    new_size = (updated_largest_dimension, updated_largest_dimension)

    resized_image = Image.new("RGB", new_size, color="white")
    box = tuple((n - o) // 2 for n, o in zip(new_size, raw_image_size))
    resized_image.paste(raw_image, box)
    return resized_image


def DigestWorkingFolder(inputPath):
    fileNames = os.listdir(inputPath)
    if fileNames.count(OUTPUT_FOLDER) == 0:
        outputPath = os.mkdir("{}\\{}".format(inputPath, OUTPUT_FOLDER))
    return fileNames


try:
        
    inputPath = input("Input folder path: ")
    additionInput = input("Enter the number of pixels to add on the widest dimension: ")
    pixelAddition = 0 if additionInput == "" else int(additionInput)
    print("The output ratio will be 1:1 (square) with border width {}".format(pixelAddition))
    
    fileNames = DigestWorkingFolder(inputPath)
    
    for file in fileNames:
        if file.endswith(".png") | file.endswith(".jpg"):
            resized_image = ResizeImage(inputPath, file, pixelAddition)
            resized_images[file] = resized_image
            resized_image.save("{}\\{}\\{}".format(inputPath, OUTPUT_FOLDER, file))
        
    print("Resizing Completed for files")
except ValueError:
    print("Provide a correct numerical value for the pixel addition")       
except:
    print("An error occurred while processing files.\nPlease confirm that the provided file path was correct")