from tkinter import *
main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

def click(event):
    across = int(c.canvasx(event.x) / 200)
    down   = int(c.canvasy(event.y) / 200)

    
    c.create_oval(
        across * 200, down * 200,
        (across + 1) * 200, (down + 1) * 200
    )

c.bind("<Button-1>", click)

mainloop()
