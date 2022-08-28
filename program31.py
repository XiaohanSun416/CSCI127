#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 27, 2022
#This program that modifies the program from Lab 7

import pandas as pd
import matplotlib.pyplot as plt

file1 = input('Enter name of input file: ')
file2 = input('Enter name of output file: ')

homeless = pd.read_csv(file1)
homeless["Fraction Children"] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
fig.savefig(file2)
