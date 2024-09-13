from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from configparser import *
import os
import AtavinAmDBMSFWWW as WWW
import webbrowser
def checkButtonActionWWW():
    WWW.createGalleryHtml()
    if enabled.get():
        webbrowser.open_new(os.path.join(os.path.abspath(WWW.data_folder), "launch.html"))
    else:
        messagebox.showinfo("Успешно", "Веб-версия БД успешно создана!")
def selectDirWWW():
    WWW.data_folder = askdirectory()
    label_m.config(text=os.path.abspath(WWW.data_folder))
def ModalDialog(title, text, geometry):
    global enabled, label_m
    enabled = IntVar()
    form_m = Toplevel(form_bd, bg="white")
    form_m.geometry(geometry)
    form_m.title(title)
    form_m.resizable(0, 0)
    label_m = Label(form_m, text=text, bg="white", anchor="center")
    label_m.place(x=5, y=10)
    if title == "WWW Галерея":
        frame_m_WWW = Frame(form_m)
        frame_m_WWW.pack(side=BOTTOM, fill=X)
        Button(form_m, text="...", command=selectDirWWW).place(x=375, y=10)
        Checkbutton(frame_m_WWW, text="Открыть выбранную БД в браузере", variable=enabled).pack(side=LEFT)
        Button(frame_m_WWW, text="Закрыть", command=form_m.destroy).pack(side=RIGHT)
        Button(frame_m_WWW, text="Создать галерею", command=checkButtonActionWWW).pack(side=RIGHT)
    form_m.grab_set()
    form_m.focus_set()
    form_m.wait_window()
def NonModalDialog():
    global fView
    fView = False
    def del_form():
        global fView
        fView = False
        form_nm.destroy()
    if not (fView):
        form_nm = Toplevel(form_bd, bg="white")
        form_nm.geometry("350x250+600+250")
        form_nm.resizable(0, 0)
        mes_nm = Message(form_nm,
                         text="Программа предназначена для визуализации файловой базы данных.\nБаза данных представляет собой папку с файлами.\n\n"
                               "Клавиши программы (которые, на самом деле, не работают):\nF1 - Вызов справки\nF2 - Добавление данных\nF3 - Удаление данных\nF4 - Изменение данных\nF10 - Меню\n\n"
                               "Авторские права:\nАтавин Даниил, Москва, 2024.\n\n"
                               "Спасибо за Ваше уделенное время!", bg="white", anchor="center")
        mes_nm.pack(side=LEFT, fill=X)
        form_nm.protocol("WM_DELETE_WINDOW", del_form)
        form_nm.focus_set()
        fView = True
def cmClick(event):
    global conf_art, photoImage, canvas, list_elements, elements, pathToDataBase
    pathToImage = pathToDataBase + '\\' + conf_art[str(elements[list_elements.curselection()[0]])]["image"]
    pathToText = pathToDataBase + '\\' + conf_art[str(elements[list_elements.curselection()[0]])]["info"]
    with open(pathToText, encoding="UTF-8") as f3:
        text_read = f3.read()

    for widget in frame_photo.winfo_children():
        widget.destroy()
    for widget in frame_text.winfo_children():
        widget.destroy()
    photoImage = PhotoImage(file=pathToImage)
    canvas = Canvas(frame_photo, scrollregion=(0, 0, 0, 0), bg="white")
    canvas.pack(side=TOP, fill=BOTH, expand=YES)
    form_bd.update()
    canvas.image = photoImage
    coef = int(round(1 / (canvas.winfo_width() / photoImage.width()), 1) * 5)
    photoImage = photoImage.zoom(5, 5)
    photoImage = photoImage.subsample(coef, coef)
    canvas.image = photoImage
    canvas.create_image(1, 1, image=photoImage, anchor=NW)
    canvas.config(scrollregion=(0, 0, 0, photoImage.height()))
    canvas_scroll = Scrollbar(frame_photo, orient=VERTICAL, command=canvas.yview)
    canvas_scroll.pack(side=RIGHT, fill=Y)
    canvas["yscrollcommand"] = canvas_scroll.set
    canvas.pack(side=LEFT, fill=BOTH, padx=1, pady=1, expand=YES)
    info = Text(frame_text, bg="white", font=('COMIC SANS MS', 15), height=5, width=150)
    info.insert(END, text_read)
    info.config(state=DISABLED)
    info_scroll = Scrollbar(frame_text, orient=VERTICAL, command=info.yview)
    info_scroll.pack(side=RIGHT, fill=Y)
    info["yscrollcommand"] = info_scroll.set
    info.pack(side=LEFT, fill=BOTH, padx=1, pady=1, expand=YES)
def exitBD():
    form_bd.destroy()
def openDB(fileName=''):
    global conf_art, elements, list_elements, pathToDataBase
    fileName = askopenfilename() if fileName == '' else fileName
    cfg = ConfigParser()
    fileName = os.path.abspath(fileName)
    path = os.path.dirname(fileName) + '\\'
    with open(fileName, encoding='UTF-8') as f1:
        cfg.read_file(f1)
    pathToDataBase = path + cfg["main"]["datapath"]
    conf_art = ConfigParser()
    elements = []
    with open(f"{pathToDataBase}\\index.ini", encoding='UTF-8') as f2:
        conf_art.read_file(f2)
    for key, value in conf_art.items():
        elements.append(key)
    elements = elements[1:]
def createAndBindElements():
    global frame_list_element, list_elements
    for widget in frame_list_element.winfo_children():
        widget.destroy()
    formElements = Variable(value=elements)
    list_elements = Listbox(frame_list_element, listvariable=formElements, font=('COMIC SANS MS', 15))
    list_elements.pack(side=LEFT, fill=BOTH, padx=1, pady=1, expand=YES)
    list_scroll = Scrollbar(frame_list_element, orient="vertical", command=list_elements.yview)
    list_scroll.pack(side=RIGHT, fill=Y)
    list_elements["yscrollcommand"] = list_scroll.set
    list_elements.bind('<<ListboxSelect>>', cmClick)
    list_elements.select_set(0)
    list_elements.event_generate("<<ListboxSelect>>")

form_bd = Tk()
W, H = 1000, 600
L, T = (form_bd.winfo_screenwidth()-W)//2, (form_bd.winfo_screenheight()-H)//2
form_bd.geometry(f"{W}x{H}+{L}+{T}")
form_bd.title("Известные города России")
mainmenu = Menu(form_bd)
form_bd.config(menu=mainmenu)
basemenu = Menu(mainmenu, tearoff=0)
basemenu.add_command(label="Открыть", command=openDB)
basemenu.add_command(label="Галерея", command=lambda: ModalDialog(title="WWW Галерея", text=f"Путь: {os.path.join(os.getcwd(), WWW.data_folder)}", geometry="400x70+750+250"))
basemenu.add_separator()
basemenu.add_command(label="Выход", command=exitBD)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Содержание", command=NonModalDialog)
helpmenu.add_separator()
helpmenu.add_command(label="О программе", command=lambda: ModalDialog(title="О программе", text="Программа предназначена для\nвизуализации файловой базы данных:\n"
                                                                                                "Известные города России\nАтавин Даниил, Москва, 2024",  geometry="225x100+750+250"))
mainmenu.add_cascade(label="База", menu=basemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
body = PanedWindow(form_bd, orient=HORIZONTAL)
frame_list_element = Frame(body)
frame_main = PanedWindow(body, orient=VERTICAL)
frame_photo = Frame(frame_main, bg='white')
frame_text = Frame(frame_main)
frame_hotkeys = Frame(form_bd)
body.pack(side=TOP, fill=BOTH, expand=YES)
frame_hotkeys.pack(side=TOP, fill=X)
frame_list_element.pack(side=LEFT, fill=BOTH)
frame_main.pack(side=LEFT, fill=BOTH, expand=YES)
frame_photo.pack(side=TOP, fill=BOTH, expand=YES)
frame_text.pack(side=BOTTOM, fill=BOTH, expand=YES)
frame_main.add(frame_photo)
frame_main.add(frame_text)
body.add(frame_list_element)
body.add(frame_main)
label_hotkeys = Label(frame_hotkeys, text="F1 - Справка F2 - Добавить F3 - Удалить F4 - Изменить F10 - Меню", bg='white', anchor="w")
label_hotkeys.pack(side=LEFT, fill=X, padx=1, pady=1, expand=YES)
form_bd.withdraw()
ModalDialog(title="Выражение благодарности",
            text="Хочу выразить благодарность моим Маме (Марии) и Папе (Антону), Бабушке (Галине) и Дедушке (Олегу) за то, что\n"
                 "воспитали во мне порядночого, доброго и заботливого человека!",
            geometry="655x60+450+300")
openDB("AmDBMSF.ini")
createAndBindElements()
list_elements.event_generate("<<ListboxSelect>>")
form_bd.deiconify()
form_bd.update()
list_elements.event_generate("<<ListboxSelect>>")
form_bd.mainloop()