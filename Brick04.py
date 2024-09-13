from tkinter import *
def cmClick():
    S = entry1.get()
    label1.config(text=S)
form1=Tk()
W, H, L, T = 320, 240, 600, 250
form1.geometry(f"{W}x{H}+{L}+{T}")
label1=Label(text="Введите фамилию:")
label1.place(x=5, y=5)

#Табуляция работает по порядку объявления

entry1=Entry(show="*")
entry1.place(x=5, y=35)

entry1.focus()

entry2=Entry(show="*")
entry2.place(x=5, y=65)

entry3=Entry(show="*")
entry3.place(x=5, y=95)

Button(text="Жмяк!", command=cmClick).place(x=5, y=125)
form1.mainloop()