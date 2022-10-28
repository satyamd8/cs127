#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 5, 2022
#This program prints: the purina logo

import turtle

t = turtle.Turtle()
t.pensize(5)
t.shape("circle")

for tColor in ["green", "blue", "cyan", "red"]:
    t.color(tColor)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
