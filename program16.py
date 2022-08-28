#Name: Xiaohan Sun
#Email: xiaohan.sun94@nyhunter.cuny.edu
#Date: March 06, 2022
#This program asks the user for 5 whole (integer) numbers

import turtle
sun = turtle.Turtle()

for i in range(5):
    num = int(input("Enter a number: "))
    sun.left(num)
    sun.forward(100)
