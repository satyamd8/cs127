#Name: Satyam Dhar
#Email: satyam.dhar58@myhunter.cuny.edu
#Date: September 17, 2022
#This program prints: two cyan circles

import turtle				

turtle.colormode(255)
h = turtle.Turtle()
h.shape("turtle")

for i in range (2):
    for i in range(0,255,10):
         h.forward(10)		
         h.pensize(i)		
         h.color(0,i,i)
    h.pensize(0)
    h.penup()
    h.backward(255)
    h.left(90)
    h.pendown()
    
