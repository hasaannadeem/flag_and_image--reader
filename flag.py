# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:07:55 2021

@author: Admin
"""

import turtle
from turtle import *

turtle.reset()
turtle.resetscreen()
turtle.clear()

screen = turtle.Screen()
screen.bgcolor("white")

a = turtle.Turtle()
turtle.title('----------Pakistani Flag----------')

a.shape('turtle')

a.reset()
a.speed(1)
a.begin_fill()
a.fillcolor("green")
a.up()
a.goto(-200, 200)
a.down()
a.forward(600)
a.setheading(to_angle=270)
a.forward(400)
a.setheading(to_angle=180)
a.forward(600)
a.setheading(to_angle=90)
a.forward(400)
a.end_fill()
a.setheading(to_angle=180)
a.forward(200)
a.setheading(to_angle=270)
a.forward(400)
a.setheading(to_angle=0)
a.forward(200)
a.up()


a.goto(160,-40)
a.color('white')
a.begin_fill()
a.circle(100)
a.end_fill()


a.goto(180,-10)
a.color('green')
a.begin_fill()
a.circle(100)
a.end_fill()

a.down()
a.goto(140,100)
a.right(20)
a.color('white', 'white')
#a.forward(100)

a.pendown()
a.color('white')
a.begin_fill()

# executing loop 5 times for a star
for i in range(5):
        # moving turtle 100 units forward
        a.forward(100)      
        # rotating turtle 144 degree right
        a.right(144)

a.end_fill()
a.up()

a.goto(175,50)
a.color('white')
a.begin_fill()
a.circle(20)
a.end_fill()

a.goto(125,-250)
a.color('green')
a.write("     PAKISTAN ZINDABAD")