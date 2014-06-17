from tkinter import *

main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

c.create_line(200, 0, 200, 600)
c.create_line(400, 0, 400, 600)

c.create_line(0, 200, 600, 200)
c.create_line(0, 400, 600, 400)

c.create_text(10, 10, text="0")
c.create_text(210, 10, text="1")
c.create_text(410, 10, text="2")
c.create_text(10, 210, text="3")
c.create_text(210, 210, text="4")
c.create_text(410, 210, text="5")
c.create_text(10, 410, text="6")
c.create_text(210, 410, text="7")
c.create_text(410, 410, text="8")

mainloop()
