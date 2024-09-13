from tkinter import *
def cmClick1():
    label1["text"]="Зима сейчас, дубина!"
    #label1.config(text="Точно-точно весна?")
form1 = Tk()

w, h = 320, 240
l, t = (form1.winfo_screenwidth()-w)//2, (form1.winfo_screenheight()-h)//2

form1.geometry(f"{w}x{h}+{l}+{t}")
form1.title("Кин-Цза-Цза")
form1.config(bg="purple")

label1 = Label(text="На улице весна?")
label1.place(x=5, y=5)

button1 = Button(text="Весна!", command=cmClick1).place(x= 5, y=35)

form1.mainloop()