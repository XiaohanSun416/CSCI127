#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 27, 2022
#This program that prompts the user to enter a list of names

nameList = input('Enter your list of names: ')

nameList = nameList.split(";")

for n in nameList:
    name = n.split(",")
    print(name[1],name[0])

print('Thank you for using my name organizer!')
