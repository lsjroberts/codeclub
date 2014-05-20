from turtle import *

size = 1

screensize(900,600)

speed(11)

penup()
setx(-900)
pendown()

def fractal(depth):
    if depth == 1:
        forward(size)
    else:
        depth = depth - 1
        fractal(depth)
        left(60)
        fractal(depth)
        right(120)
        fractal(depth)
        left(60)
        fractal(depth)

fractal(8)

exitonclick()