from tkinter import *
def cmClick1(e):
    label1['text']="Мы сидим на паре с преподавателем по имени " + listbox1.get(listbox1.curselection())
form1 = Tk()
w, h, l, t = 320, 240, 600, 250
form1.geometry(f"{w}x{h}+{l}+{t}")
label1 = Label(text="Что тебе больше по душе?")
label1.place(x=5, y=5)
ls=["Оклик", "Медведь", "Велес", "Сварог", "Перун"]
listbox1=Listbox()
for i in range (len(ls)):
    listbox1.insert(END, ls[i])
listbox1.place(x=5, y=35)
listbox1.bind("<<ListboxSelect>>", cmClick1)
form1.mainloop()