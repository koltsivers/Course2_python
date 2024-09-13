from tkinter import *
def cmCliked():
    ...
form1 = Tk()
W, H, L, T = 320, 240, 600, 250
form1.geometry(f"{W}x{H}+{L}+{T}")
form1.configure(bg='DarkOliveGreen1')

frame1 = Frame()
frame1.pack(side=BOTTOM)

frame2 = Frame()
frame2.pack(side=TOP)

label1 = Label(frame2, text='label1')
label1.pack()

label2 = Label(frame1, text='label2')
label2.pack()

label3 = Label(frame1, text='label3')
label3.pack()

form1.mainloop()