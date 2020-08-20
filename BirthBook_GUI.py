from tkinter import *
import os

birth_book = dict()
name_list = list()

def clear():
    input_name.delete(0, END)
    input_day.delete(0, END)
    input_month.delete(0, END)
    input_year.delete(0, END)

def add():
    name = input_name.get()
    if name in birth_book:
        label_info.config(text="Такое имя уже существует")
    else:
        value = list()
        value.append(input_day.get())
        value.append(input_month.get())
        value.append(input_year.get())
        birth_book[input_name.get()] = value

        list_name.insert(END, name)

def select_list_name(evt):
    w = evt.widget
    i = int(w.curselection()[0])
    name = w.get(i)

    value = birth_book[name]
    day = value[0]
    month = value[0]
    year = value[0]

    input_name.insert(0, name)
    input_day.insert(0, day)
    input_month.insert(0, month)
    input_year.insert(0, year)

window = Tk()
window.title("BirthBook")
window.geometry("500x250")

# Объявление элементов окна
label_name = Label(text="Имя")
input_name = Entry()

label_day = Label(text="День")
input_day = Entry()
label_month = Label(text="Меяц")
input_month = Entry()
label_year = Label(text="Год")
input_year = Entry()

label_name.grid(row=0, column=0, padx=10, pady=5)
button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)
button_edit = Button(text="Редактировать")# command=edit
button_quit = Button(text="Выйти")# command=quit

label_list_name = Label(text="Список дней рождений")
list_name = Listbox()

label_info = Label(text="Программа готова к работе")

# Позиционирование
label_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")
input_name.grid(row=1, column=1)

label_day.grid(row=2, column=0, padx=5, pady=5, sticky="e")
input_day.grid(row=2, column=1, padx=10)

label_month.grid(row=3, column=0, padx=5, pady=5, sticky="e")
input_month.grid(row=3, column=1)

label_year.grid(row=4, column=0, padx=5, pady=5, sticky="e")
input_year.grid(row=4, column=1, padx=10)

button_add.grid(row=1, column=2, padx=20)
button_edit.grid(row=2, column=2, padx=20)
button_clear.grid(row=3, column=2, padx=20)
button_quit.grid(row=4, column=2, padx=20)

label_list_name.grid(row=2, column=3)
list_name.grid(row=1, column=3, rowspan=4)

label_info.grid(row=0, column=1, columnspan=4, sticky="w")

list_name.bind('<<ListboxSelect>>', select_list_name)

if os.path.exists("BirthBook.csv"):
    with open("BirthBook.csv", "r") as file:
        lines - file.readlines()
        for line in lines:
            elements = line.split(";")
            name = elements[0]
            day = elements[1]
            month = elements[2]
            year = elements[3]
            value = list()
            value.append(day)
            value.append(month)
            value.append(year)
            phone_book[name] = value
            list_name.insert(END, name)

window.mainloop()
