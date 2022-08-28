#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 15, 2022
#This program asks the user for the name of a png file and print the number of pixels that are nearly white

import matplotlib.pyplot as plt
import numpy as np

s = input("Enter a name of image: ")
ca = plt.imread(s)
countSnow = 0
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow = countSnow + 1
print("Snow count is", countSnow)

