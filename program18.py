#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 07, 2022
#This program creates a image of red and white stripes

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter size of the image: "))
img = np.ones((num,num,3))
name = input("Enter name of this file: ")
img[::2,:,1:] = 0

plt.imsave(name,img)
