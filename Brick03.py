from tkinter import *
def cmClick1():
    #label1["text"]="Зима сейчас, дубина!"
    S=text1.get(1.0, 2.0)
    label1.config(text=S)
form1 = Tk()

w, h = 320, 240
l, t = (form1.winfo_screenwidth()-w)//2, (form1.winfo_screenheight()-h)//2

form1.geometry(f"{w}x{h}+{l}+{t}")
form1.title("Кин-Цза-Цза")
form1.config(bg="green")

label1 = Label(text="Амогус!")
label1.place(x=5, y=5)

#entry1 = Entry(show="*")
#entry1.place(x=5, y=35)
Button(text="Жмяк!", command=cmClick1).place(x= 5, y=35)

text1 = Text(width=38, height=10)
text1.place(x=5, y = 65, width=310, height=170)
for i in range (1, 11):
    text1.insert(END, f"Чупакабра{i}\n")
text1.insert(END, "Чупакабра!")

form1.mainloop()