#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 21, 2022
#This program prints: pink eye

import turtle

turtle.colormode(255)
h = turtle.Turtle()
h.backward(100)

for i in range (0, 255, 10):
    h.forward(10)
    h.pensize(i)
    h.color(i, 0, i)

for i in range (255, 0, -10):
    h.forward(10)
    h.pensize(i)
    h.color(i, 0, i)

