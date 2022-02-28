import matplotlib.image as mpimg
import numpy as np
from math import *
import sys

"""
----------------------- Mandelbrot set --------------------
Author: Mounir LBATH
Version: 1.0
Creation Date: 06/2021
-----------------------------------------------------------
"""

# Name the images with increasing ids stocked in ImageId.txt
def ImageName(change = True):
    fin = open("ImageId.txt", "r")
    a = fin.read()
    fin.close()
    if change:
        fout = open("ImageId.txt", "w")
        fout.write(str(int(a)+1))
        fout.close()
    zeros = '0' * (3 - len(a))
    return 'render' + zeros + a + '.png'

# compute if the sequence diverges and when
def divSpeed(c, maxstep):
    i = 0
    z = c
    while i < maxstep and z.real*z.real+z.imag*z.imag <= 6:
        ########## recursion formula #############

        # Classic Mandelbrot
        z = z*z+c 
        '''
        # z=cos(z/c) (complex cosine)
        if c!=0:
            z = cos((z/c).real)*cosh((z/c).imag)-complex(0,1)*sin((z/c).real)*sinh((z/c).imag) '''
        i += 1
    return i

# color the pixels depending on divergence speed
def color(speed, maxstep):
    return [1-speed/maxstep,1-speed/maxstep,1-speed/maxstep] # black and white coloring, can be changed

# plot the image and save it into a png file
def plot(maxstep, w=500, h=500):
    img = np.zeros((h, w,3))

    # bottom left corner of the interval x and y coord, interval length along x axis

    length, coord = 3, [-2.25,-1.5] # all the shape
    '''
    length = 3; coord = [-length/2,-length*h/(2*w)] # centered on 0
    length, coord = 0.5, [-0.5,0.5] # nice interval
    length, coord = 0.075, [-0.27,0.7] # nice interval
    length, coord = 0.025, [-0.2425,0.7075] # nice interval
    length, coord = 0.006, [-0.2303,0.7239] # nice interval'''

    mapper = lambda x,y : (coord[0]+length*x/(w),coord[1]+length*y/w) 

    # compute each pxl
    for x in range(w):
        for y in range(h):
            speed = divSpeed(complex(*mapper(x,h-y-1)), maxstep)
            img[y][x] = color(speed, maxstep)
            
            # loading bar, slows down computations
            #sys.stdout.write("\r\t[{}{}]{}%".format("■" * (int(50*(x*h+y)/(w*h))+1)," " * (49-int(50*(x*h+y)/(w*h))), 100*(x*h+y)/(w*h)))

    # Create the image
    mpimg.imsave(ImageName(True), img)

# Change the parameters : computation quality, pxl width, pxl height
plot(150, 500,500)
