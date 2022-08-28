#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 21, 2022
#This program asks the user for the borough, an name for the output file, and then display the fraction of the population that has lived in that borough, over time

import matplotlib.pyplot as plt
import pandas as pd

boro = input('Enter borough name: ')
name = input('Enter the name of file: ')

pop = pd.read_csv('nycHistPop.csv' ,skiprows=5)
pop['Fraction'] = pop[boro]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(name)
