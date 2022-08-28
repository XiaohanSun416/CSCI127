#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhunter.cuny.edu
#Date: April 03, 2022
#This program is a template program that draw nestedtriangle

import turtle
sun = turtle.Turtle()

def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)

def triangle(t, length):
    if(length > 10):
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def nestedTriangle(t, length):
    if(length > 10):
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)

def main():
    mess = int(input('Enter the length: '))

if __name__ == "__main__":
    main()
