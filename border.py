from PIL import Image
import os
OUTPUT_FOLDER = "processed_images"


def ResizeImage(inputPath, fileName, pixelAddition, ratio):
    raw_image = Image.open("{}/{}".format(inputPath, fileName))
    raw_image_size = raw_image.size
    width = raw_image_size[0]
    largest_dimension = max(raw_image_size)

    updated_largest_dimension = largest_dimension + pixelAddition * 2
    updated_shortest_dimension = int(round(updated_largest_dimension*ratio, 0))

    if (width == largest_dimension):
        new_size = (updated_largest_dimension, updated_shortest_dimension)
    else:
        new_size = (updated_shortest_dimension, updated_largest_dimension)

    resized_image = Image.new("RGB", new_size, color="white")
    box = tuple((n - o) // 2 for n, o in zip(new_size, raw_image_size))
    resized_image.paste(raw_image, box)

    return resized_image


def DigestWorkingFolder(inputPath):
    fileNames = os.listdir(inputPath)
    filteredNames = []
    if fileNames.count(OUTPUT_FOLDER) == 0:
        outputPath = os.mkdir("{}\\{}".format(inputPath, OUTPUT_FOLDER))

    for file in fileNames:
        if file.endswith(".png") or file.endswith(".jpg"):
            filteredNames.append(file)

    return filteredNames


def Resize(inputPath):
    additionInput = input(
        "Enter the number of pixels to add on the widest dimension (default 300px): ")
    rawLongRatio = input("Input length of ratio (eg: the 3 in 3:2)    ")
    rawWidthRatio = input("Input width of ratio (eg: the 2 in 3:2)    ")
    longRatio = max(((int(rawLongRatio)), int(rawWidthRatio)))
    widthRatio = min(((int(rawLongRatio)), int(rawWidthRatio)))
    ratio = int(widthRatio)/int(longRatio)
    pixelAddition = 300 if additionInput == "" else int(additionInput)

    print("\nThe output ratio will be {}:{} with a standard border addition of {}\n".format(longRatio, widthRatio,
                                                                                            pixelAddition))
    fileNames = DigestWorkingFolder(inputPath)

    print("Resizing {} pictures".format(len(fileNames)))
    i = 1

    for file in fileNames:

        print("Resizing picture {} of {}".format(i, len(fileNames)))
        resized_image = ResizeImage(inputPath, file, pixelAddition, ratio)

        resized_image.save("{}\\{}\\{}".format(inputPath, OUTPUT_FOLDER, file))

        i += 1
    print("Resizing Completed for all files")


try:
    inputPath = input("Input folder path: ")

    while (inputPath != ""):
        Resize(inputPath)
        inputPath = input("Input folder path: ")


except ValueError:
    print("Provide a correct numerical value for the pixel addition")
except:
    print("An error occurred while processing files.\nPlease confirm that the provided file path was correct")
finally:
    os.system("pause")
