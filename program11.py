#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: February 20, 2022
#This program modifies the program from Lab3 to show the shades of blue

import turtle

turtle.colormode(255)
sun = turtle.Turtle()
sun.shape("turtle")
sun.backward(100)

for i in range(0,255,10):
    sun.forward(10)
    sun.pensize(i)
    sun.color(0,0,i)
