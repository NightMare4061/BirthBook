import datetime
import os

date_time = datetime.datetime.now()

def log(msg):
    with open("BirthBook.log", "a") as file:
        message = date_time.strftime("%Y-%m-%d %H:%M") + " : " + msg + "\n"
        file.write(message)

def input_data():
    temp = list()
    day = input("Введите день: ")
    month = input("Введите месяц: ")
    year = input("Введите год: ")
    print("===== ===== =====")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(patronymic)
    temp.append(address)
    return temp

def welcome():
    print("*" * 41)
    print("*** BirthBook - телефонный справочник ***")
    print("*" * 41)
    log("Программа запустилась")

def menu():
    print("===== ===== ====")
    print("Режим работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Сохранить в файл")
    print("0. Выход")

def show(birth_book):
    print("--- Телефонный справочник ---")
    for tel in birth_book:
        value = birth_book[tel]
        temp = value[0] + "" + value[1] + "" + value[2] + ", " + value[3]
        print(tel, ":", temp)
    print("===== ===== =====")
    log("Вывод справочника на экран")

def save(birth_book):
    with open("BirthBook.csv", "w") as file:
        for tel in birth_book:
            value = birth_book[tel]
            temp = tel + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
            file.write(temp)


def delete(birth_book):
    print("Введите номер телефона для удаления: ")
    if tel in birth_book:
        note = birth_book.pop(tel)
        print("# Запись " + tel + " удалена #")
        log("Запись с " + tel + " успешно удалена")
    else:
        print("# Вы ввели неправильный номер #")
        log("Неудачная попытка удаления записи с номером " + tel)


def input_(birth_book):
    tel = input("Введите номер телефона: ")
    if tel in birth_book:
        print("# Такой номер уже существует")
        log("Неудачная попытка добавления записи с номером " + tel)
    else:
        value = input_data()
        birth_book[tel] = value
        print("# Запись успешно добавлена #")
        log("Запись с " + tel + " успешно добавлена")

def edit(birth_book):
    tel = input("Введите номер телефона: ")
    if tel in birth_book:
        temp = input_data()
        birth_book[tel] = temp
        print("# Запись успешно изменена #")
        log("Запись с " + tel + " успешно изменена")
    else:
        print("# Вы ввели неправильный номер #")
        log("Неудачная попытка редактирования записи с номером " + tel)

def import_(birth_book):
    if os.path.exists("BirthBook.csv"):
        with open("BirthBook.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                elements = line.split(";")
                tel = elements[0]
                last_name = elements[1]
                first_name = elements[2]
                patronymic = elements[3]
                address = elements[4]
                value = list()
                value.append(last_name)
                value.append(first_name)
                value.append(patronymic)
                value.append(address)
                birth_book[tel] = value
        log("Импорт из файла")
    else:
        log("Файл для импорта не найден")
