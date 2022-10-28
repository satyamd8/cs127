#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 21, 2022
#This program prints: brown triangle

import turtle

h = turtle.Turtle()
h.shape("turtle")
turtle.colormode(255)
h.color(150, 75, 0)
h.pensize(2)

for i in range(3):
    h.forward(100)
    h.left(120)
    h.stamp()
