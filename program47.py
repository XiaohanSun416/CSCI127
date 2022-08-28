#Name: Xiaohan Sun
#Email: xiaohan.sun94@myhuntercuny.edu
#Date: April 22, 2022
#This program that modifies the prorgam from Lab 10

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(360)
  trey.right(a)
