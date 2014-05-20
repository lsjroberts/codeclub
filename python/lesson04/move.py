from turtle import *

print("Move 10 steps")


# The sprite starts at x_position 0
x_position = 0


# This method moves the sprite a number of steps
def move(steps):
    x_position = x_position + steps


# Calling the `move` method with a value of 10 will
# move the sprite 10 steps
move(10)

# Calling the `move` method with a value of -5 will
# move the sprite 5 steps in the opposite direction
move(-5)
