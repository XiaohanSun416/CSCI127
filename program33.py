#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 27, 2022
#This program that writes a program that asks the user for the name of an image, the name of an output file

import matplotlib.pyplot as plt
import numpy as np

image1 = input('Enter name of input file: ')
image2 = input('Enter name of output file: ')

img = plt.imread(image1)
height = img.shape[0]
width = img.shape[1]
img2 = img[height//2:, :width//2]

plt.imsave(image2, img2)
