#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 03, 2022
#This program modifes the parking ticket program from Lab 8

import pandas as pd

csvFile = input('Enter CSV file name: ')
attribute = input('Enter attribute: ')
name = pd.read_csv(csvFile)
print("The 10 worst offenders are:")
print(name[attribute].value_counts()[:10])
