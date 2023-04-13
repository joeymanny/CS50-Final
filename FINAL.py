from PIL import Image
from math import sqrt
import numpy as np
# mandelbrot function
def mandel(x, y):
    c = complex(x, y)
    z = 0
    it = 0
    # low iteration count for speed
    for i in range(100):
        z = (z * z) + c
        it += 1
    if 2 >  sqrt((z.real * z.real) + (z.imag * z.imag)):
        # part of the set
        return -1
    # not part of the set; return number of iterations
    return it
# unneccessary function; saved for future feature implementation
def mandelcolor(it):
    if it == -1:
        return 0
    else:
        return int(0xffffff) 
# main prompt loop
while True:
    #input
    width = int(input("resolution: "))
    height = width
    xslide = float(input("x slide: "))
    yslide = float(input("y slide: "))
    # initializin array in the shape desired
    coords = np.zeros((height, width))
    # for each item in the array (every pixel)
    for y in range(len(coords)//-2, len(coords)):
        for x in range(len(coords[y])//-2, len(coords[y])):
            # calculate its color (whether it is a part of the set) and add it to the array
            coords[y][x] = mandelcolor(mandel(x/len(coords[y]) * 2.4 - 1.7 + xslide, y/len(coords) * 2.4 - 1.2 - yslide)) 
    # copy array to a PNG image
    Image.fromarray(coords).show()
