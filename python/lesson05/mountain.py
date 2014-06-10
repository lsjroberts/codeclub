from turtle import *

def mountain(depth):
    if depth == 1:
           forward(30)
    else:
        newdepth = depth -1
        mountain(newdepth)
        left(60)
        mountain(newdepth)
        right(120)
        mountain(newdepth)
        left(60)
        mountain(newdepth)

mountain(46)
