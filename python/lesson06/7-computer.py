from tkinter import *
import random

main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

grid = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8",
]

def click(event):
    global shape, grid
    across = int(c.canvasx(event.x)/200)
    down = int(c.canvasy(event.y)/200)

    square = across + (down*3)

    if grid[square] == "X" or grid[square] == "O":
        return

    if winner(grid):
        return

    c.create_oval(
        across*200,down*200,
        (across+1)*200,(down+1)*200
    )

    grid[square] = "O"

    if winner(grid):
        return

def winner(grid):
    for across in range(3):
        row = across*3
        line = grid[row] + grid[row+1] + grid[row+2]

        if line == "XXX" or line == "OOO":
            return True

    for down in range(3):
        line = grid[down] + grid[down+3] + grid[down+6]

        if line == "XXX" or line == "OOO":
            return True

    line = grid[0]+grid[4]+grid[8]

    if line == "XXX" or line == "OOO":
        return True

    line = grid[2]+grid[4]+grid[6]

    if line == "XXX" or line == "OOO":
        return True

def play_move():
    move = -1
    moves = free_squares()

    if not moves:
        return

    # find winning move if exists
    for possible in moves:
        new_grid = list(grid)
        new_grid[possible] = "X"

        if winner(new_grid):
            move = possible
            break

    if move < 0:
        for possible in moves:
            new_grid = list(grid)
            new_grid[possible] = "O"

            if winner(new_grid):
                move = possible
                break

    if move < 0:
        move = random.choice(moves)

    across, down = move%3, move//3

    grid[move] = "X"

    c.create_line(
        across*200, down*200,
        (across+1)*200, (down+1)*200
    )

    c.create_line(
        across*200, (down+1)*200,
        (across+1)*200, down*200
    )

def free_squares():
    output = []

    for position, square in enumerate(grid):
        if square != "X" and square != "O":
            output.append(position)

    return output

c.bind("<Button-1>", click)

mainloop()
