#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: February 22, 2022
#This program asks the user for a name of an image .png file and the name of an output file

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

image = input("Enter name of the input file: ")
img = plt.imread(image)

output = input("Enter name of the output file: ")
img2 = img.copy()
img2[:,:,0] = 0
img2[:,:,1] = 0

plt.imsave(output, img2)
