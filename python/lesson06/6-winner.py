from tkinter import *

main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

shape = "O"
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

    if winner():
        return

    if shape == "O":
        c.create_oval(
            across * 200, down * 200,
            (across + 1) * 200, (down + 1) * 200
        )
        grid[square] = "O"
        shape = "X"
    else:
        c.create_line(
            across * 200, down * 200,
            (across + 1) * 200, (down + 1) * 200
        )
        c.create_line(
            across * 200, (down + 1) * 200,
            (across + 1) * 200, down * 200
        )
        grid[square] = "X"
        shape = "O"

def winner():
    # Check each horizontal row for all the same player
    for across in range(3):
        row = across*3
        line = grid[row] + grid[row+1] + grid[row+2]
        if line == "XXX" or line == "OOO":
            return True

    # Check each vertical column for all the same player
    for down in range(3):
        line = grid[down] + grid[down+3] + grid[down+6]
        if line == "XXX" or line == "OOO":
            return True

    # Check top-left to bottom-right diagonal
    line = grid[0]+grid[4]+grid[8]
    if line == "XXX" or line == "OOO":
            return True

    # Check bottom-left to top-right diagonal
    line = grid[2]+grid[4]+grid[6]
    if line == "XXX" or line == "OOO":
            return True

c.bind("<Button-1>", click)

mainloop()
