from tkinter import *
def cmClick1():
    print(s.get())
    label1['text']="Мы сидим на паре с преподавателем по имени " + ls[s.get()]
form1 = Tk()
w, h, l, t = 320, 240, 600, 250
form1.geometry(f"{w}x{h}+{l}+{t}")
label1 = Label(text="Как зовут преподавателя?")
label1.place(x=5, y=5)
s=IntVar()
ls=["Оля", "Юля", "Олег"]
#checkbutton1=Checkbutton(variable=s) #, command=cmClick1
#checkbutton1.place(x=5, y=35)

radiobutton1=Radiobutton(text=ls[0], variable=s, value=0, command=cmClick1)
radiobutton1.place(x=5, y=35)

radiobutton2=Radiobutton(text=ls[1], variable=s, value=1, command=cmClick1)
radiobutton2.place(x=5, y=65)

radiobutton3=Radiobutton(text=ls[2], variable=s, value=2, command=cmClick1)
radiobutton3.place(x=5, y=95)

button1 = Button(text="Хочу знать...", command=cmClick1).place(x= 5, y=125)
form1.mainloop()