# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from BirthBook_lib import *

birtn_book = dict()

welcome()

#import_(birth_book)

while True:
    menu()
    choice = (input("Введите режим работы: "))

    if choice == "1":
        show(birth_book)

    elif choice == "2":
        input_(birth_book)

    elif choice == "3":
        edit(birth_book)

    elif choice == "4":
        delete(birth_book)

    elif choice == "5":
        save(birth_book)

    elif choice == "0":
        print("До свидания!")
        log("Выход из программы")
        break

    else:
        print("Ошибка")
        log("Неправильный режим")
