from PIL import Image
from math import sqrt
import numpy as np
def mandel(x, y):
    c = complex(x, y)
    z = 0
    it = 0
    for i in range(100):
        z = (z * z) + c
        it += 1
    if 2 >  sqrt((z.real * z.real) + (z.imag * z.imag)):
        return -1
    return it
def mandelcolor(it):
    if it == -1:
        return 0
    else:
        return int(0xffffff) 
while True:
    width = int(input("resolution: "))
    height = width
#    mult = float(input("multiplier: "))
    xslide = float(input("x slide: "))
    yslide = float(input("y slide: "))
#width_hf = width//2
#height_hf = height//2
    coords = np.zeros((height, width))

#for y in range(-1*width_hf, width_hf):
#    for x in range(-1*height_hf, height_hf):
#        print(str(x), str(x))
#        coords[abs(y)*2][abs(x)*2] = mandelcolor(mandel(x, y))

    for y in range(len(coords)//-2, len(coords)):
        for x in range(len(coords[y])//-2, len(coords[y])):
            coords[y][x] = mandelcolor(mandel(x/len(coords[y]) * 2.4 - 1.7 + xslide, y/len(coords) * 2.4 - 1.2 - yslide)) 
    Image.fromarray(coords).show()

#multiplier: 2.4
#x slide: 1.7
#y slide: 1.2