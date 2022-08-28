#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhuntercuny.edu
#Date: April 22, 2022
#This program that asks the user to enter a string

while True:
    king = input('Enter a non-empty string: ')

    if king:
        print('You entered: %s' % king)

        break
    else:
        print('That was empty. Try again.')
