#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 03, 2022
#This program writes a program that asks the user for a CSV of collision data

import pandas as pd

csvFile = input('Enter CSV file name: ')
name = pd.read_csv(csvFile)
print("The top three contributing factors for collisions are: ")
print(name['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()[:3])
