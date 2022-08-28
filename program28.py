#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 21, 2022
#This program computes the average and maximum population over time for a borough

import matplotlib.pyplot as plt
import pandas as pd

boro = input('Enter borough name: ')
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("Mean", pop[boro].mean())
print("Max", pop[boro].max())

print(df['Total'].mean())
