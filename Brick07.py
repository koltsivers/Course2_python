from tkinter import *
def cmClick1():
    canvas1.create_line(20, 10, 60, 50)
def cmMove(m):
    x, y = m.x, m.y
    canvas1.create_line (x-5, y-5, x+5, y+5, fill="cyan")
form1 = Tk()
w, h, l, t = 320, 240, 600, 250
form1.geometry(f"{w}x{h}+{l}+{t}")
form1.config(bg="purple")
canvas1=Canvas()
canvas1.config(bg="green")
canvas1.place(x=5, y=35, width=300, height=200)
canvas1.bind("<B1-Motion>", cmMove)
Button(text="Хочу построить дом", command=cmClick1).place(x= 5, y=5)
form1.mainloop()