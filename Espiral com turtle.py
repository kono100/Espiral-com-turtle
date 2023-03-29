

import random
import turtle
colors =['cyan']
t = turtle.Turtle()
t.speed(1000.000)
turtle.bgcolor("black")
lenght=1000
angle = 50
size=4.5
for i in range(lenght):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i*1)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")