#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: March 15, 2022
#This program modify a program to allow the user also to specify with the following symbols

import turtle
sun = turtle.Turtle()
myWin = turtle.Screen()
commands = input("Please enter a command string: ")

for c in commands:
    if c == 'F':
        sun.forward(50)
    elif c == 'L':
        sun.left(90)
    elif c == 'R':
        sun.right(90)
    elif c == '^':
        sun.penup()
    elif c == 'v':
        sun.pendown()
    elif c == 'B':
        sun.backward(50)
    elif c == 'S':
        sun.stamp()
    elif c == 'l':
        sun.left(45)
    elif c == 'r':
        sun.right(45)
    elif c == 'p':
        sun.color('purple')
    else: 
        print("Error: do not know the command:", i)

print("See graphics window for your image")
myWin.exitonclick()
