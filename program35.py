#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 27, 2022
#This program asks the user for the hour of the day (in 24 hour time), and prints

hours = int(input('Enter the hour of the day: '))
if hours < 12:
    print('Good Morning')
elif 12 <= hours < 17:
    print('Good Afternoon')
else:
    print('Good Evening')
