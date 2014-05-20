from turtle import *
import random

screensize(1800,900,"black")

screen = getscreen()
screen.colormode(255)

shape("circle")
pensize(1)
speed(11)

draw_color = [255,180,0]

def polygon(sides=3, length=100, rotation=0):
    angle = 360 / sides
    right(rotation)
    for count in range(sides):
        forward(length)
        right(angle)

def triangle(length, rotation):
    shape(3, length, rotation)

def hexagon(length, rotation):
    shape(6, length, rotation)

while(True):
    angle = random.randint(-20,20)
    length = random.randint(10,30)

    for i in range(3):
        new = draw_color[i] + random.randint(-20,20)
        if new < 0: new = 0
        if new > 255: new = 255
        draw_color[i] = new

    x,y = position()
    screen_x,screen_y = screen.screensize()

    color(tuple(draw_color))

    penup()
    right(angle)
    forward(length)
    pendown()
    # begin_fill()
    # setheading(0)
    triangle(length,0)
    # end_fill()

    if x < -screen_x/2:
        penup()
        x = setx(screen_x/2)
        pendown()
    if x > screen_x/2:
        penup()
        x = setx(-screen_x/2)
        pendown()
    if y < -screen_y/2:
        penup()
        y = sety(screen_y/2)
        pendown()
    if y > screen_y/2:
        penup()
        sety(-screen_y/2)
        pendown()

exitonclick()