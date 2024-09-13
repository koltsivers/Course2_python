from tkinter import *
def cmClick1():
    label1['text']="++++++"
form1 = Tk()
w, h, l, t = 320, 240, 600, 250
form1.geometry(f"{w}x{h}+{l}+{t}")
label1 = Label(text="...")
label1.place(x=5, y=5)
button = Button(text="+++", command=cmClick1).place(x= 5, y=35)
form1.mainloop()