from tkinter import *
def buttonClicked(item):
    global calculation, number1, number2
    if item in list_vars:
        if calculation == '':
            number1 += item
            label_field.configure(text=number1)
        else:
            number2 += item
            label_field.configure(text=number2)
    elif item in list_two_operations and calculation != '' and number2 != '':
        if calculation == '+':
            number1 = str(float(number1) + float(number2))
        elif calculation == '-': number1 = str(float(number1) - float(number2))
        elif calculation == '×': number1 = str(float(number1) * float(number2))
        elif calculation == '÷':
            if number2 == '0': number1 = ''
            else: number1 = str(float(number1) / float(number2))
        elif calculation == '%': number1 = str((float(number2) / (float(number1))/100)*100)
        label_field.configure(text='Ошибка, деление на 0!') if number2 == '0' else label_field.configure(text=number1)
        number2 = ''
    elif item in list_two_operations and number2 == '':
        calculation = item
        label_field.configure(text=number1)
    elif item == 'CE':
        if number1 != '' and number2 == '':
            number1 = ''
            label_field.configure(text=number1)
        elif number2 != '':
            number2 = ''
            label_field.configure(text=number2)
    elif item == '←':
        if number1 != '' and number2 == '':
            number1 = number1[0:-1]
            label_field.configure(text=number1)
        elif number2 != '':
            number2 = number2[0:-1]
            label_field.configure(text=number2)
    elif item in list_one_operations and number2 == '':
        if item == '√':
            if float(number1) > 0:
                number1 = str(float(number1)**0.5)
                label_field.configure(text=number1)
            else: label_field.configure(text='Ошибка ввода числа!')
        elif item == 'x²':
            number1 = str(float(number1)**2)
            label_field.configure(text=number1)
        elif item == '1/x':
            if number1 == '0': label_field.configure(text='Ошибка, деление на 0!')
            else:
                number1 = str(1 / float(number1))
                label_field.configure(text=number1)
        elif item == 'C':
            number1, number2, calculation = '', '', ''
            label_field.configure(text='')
        elif item == '±':
            number1 = str(float(number1) * -1)
            label_field.configure(text=number1)
        elif item == ',':
            if number1.count('.') != 1:
                number1 += '.'
                label_field.configure(text=number1)
            else:
                number1 = ''
                label_field.configure(text='Ошибка ввода числа!')
root = Tk()
W, H = 300, 450
L, T = (root.winfo_screenwidth()-W)//2, (root.winfo_screenheight()-H)//2
root.geometry(f"{W}x{H}+{L}+{T}")
root.title("Калькулятор")
root.config(bg='DarkOliveGreen1')
for i in range(7): root.rowconfigure(index=i, weight=1)
for i in range(4): root.columnconfigure(index=i, weight=1)
calculation, number1, number2, list_vars, list_two_operations, list_one_operations = '', '', '',('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), ('=', '÷', '×', '-', '+', '%'), ('√', 'x²', '1/x', 'C', '±', ',')
label_field = Label(text=number1, relief=SUNKEN, borderwidth=5, anchor='e', font=('Arial', 18))
label_field.grid(row=0, column=0, columnspan=4, sticky='nsew')
buttons = (' %', '√', 'x²', '1/x', 'CE', 'C', '←', '÷', '7', '8', '9', '×', '4', '5', '6', '-', '1', '2', '3', '+', '±', '0', ',', '=')
row_button, column_button = 1, 0
for button in buttons:
    button_print = Button(text=button, command=lambda x=button: buttonClicked(x), font=('Arial', 20), bg='DarkOliveGreen3').grid(row=row_button, column=column_button, sticky='nsew')
    column_button += 1
    if column_button > 3:
        column_button = 0
        row_button += 1
root.mainloop()