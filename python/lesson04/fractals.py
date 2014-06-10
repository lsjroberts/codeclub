from turtle import *

size = 6

screensize(900,600)
bgcolor('black')

speed(11)

penup()
setx(-400)
pendown()

def fractal(depth):
    if depth == 1:
        forward(size)
    else:
        depth = depth - 1
        fractal(depth)
        left(80)
        fractal(depth)
        right(160)
        fractal(depth)
        left(80)
        fractal(depth)

pencolor('orange')
pensize(2)
# fillcolor('orange')
# begin_fill()
for i in range(3):
    fractal(6)
    right(120)
# end_fill()


exitonclick()