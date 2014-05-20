from turtle import *
import random

screensize(1800,900,"black")

shape("circle")
speed(11)

def polygon(sides=3, length=100, rotation=0):
    angle = 360 / sides
    right(rotation)
    for count in range(sides):
        forward(length)
        right(angle)

def triangle(length, rotation):
    polygon(3, length, rotation)

def square(length, rotation):
    polygon(4, length, rotation)

def hexagon(length, rotation):
    polygon(6, length, rotation)

def circle(size):
    polygon(36, size / 11.4) # dunno why it's 11.4

def flower(x, y, number_of_petals):
    penup()
    setx(x)
    sety(y)
    pendown()

    for count in range(number_of_petals):
        setx(x)
        sety(y)
        setheading(0)
        hex_code = "#" \
            + "".join([hex(random.randint(8,15)).lstrip("0x") for i in range(2)]) \
            + "".join([hex(random.randint(3,10)).lstrip("0x") for i in range(2)]) \
            + "".join([hex(random.randint(1,3)).lstrip("0x") for i in range(2)])
        color(hex_code)
        begin_fill()
        triangle(300, count * (360 / number_of_petals))
        end_fill()

flower(0, 200, 6)
flower(-400, 0, 12)
flower(0, -200, 24)
flower(400, 0, 48)

exitonclick()