"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------


"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    pass


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pass


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    pass


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for y in range(height):
        for x in range(width):
            sum_red = sum_green = sum_blue = 0
            maxdistance = 1000
            for i in range(len(images)):
                sum_red += images[i].get_pixel(x,y).red
                sum_green += images[i].get_pixel(x, y).green
                sum_blue += images[i].get_pixel(x, y).blue
            avg_red = sum_red/len(images)
            avg_green = sum_green/len(images)
            avg_blue = sum_blue / len(images)
            for j in range(len(images)):
                if maxdistance > ((avg_red-images[j].get_pixel(x,y).red)**2 + (avg_green-images[j].get_pixel(x,y).green)**2 + (avg_blue-images[j].get_pixel(x,y).blue)**2)**0.5:
                    result.get_pixel(x,y).red = images[j].get_pixel(x,y).red
                    result.get_pixel(x, y).green = images[j].get_pixel(x, y).green
                    result.get_pixel(x, y).blue = images[j].get_pixel(x, y).blue
                    maxdistance = ((avg_red - images[j].get_pixel(x, y).red) ** 2 + (avg_green - images[j].get_pixel(x, y).green) ** 2 + (avg_blue - images[j].get_pixel(x, y).blue) ** 2) ** 0.5
        if y%int(height/100) == 0:
            print("loading..."+str(y//(height/100)+1)+"%")
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)

if __name__ == '__main__':
    main()
