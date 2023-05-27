from main import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
while enter != 6:
    enter = interface()
    if enter == 1:
        from main import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
    elif enter == 2:
        from main import show_all
        print(show_all(path))
    elif enter == 3:
        from main import search
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
    elif enter == 4:
        from main import delete
        delete(path)
    elif enter == 5:
        from main import izm
        izm(path)
    print("спасибо за работу")