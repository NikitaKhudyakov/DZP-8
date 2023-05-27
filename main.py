path = "phone_book.txt"
def create(path):
    try:
        file = open(path, 'r+')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka):
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()

def delete(path):
    print("CПРАВОЧНИК")
    with open(path, "r") as data:
        book = data.read()
        print(book)
   
    index = int(input("Введите номер строки для удаления: ")) - 1
    book_lines = book.split("\n")
    deleted = book_lines[index]
    book_lines.pop(index)
    print(f"Удалена запись: {deleted}\n")
    with open(path, "w", encoding='utf-8') as data:
        data.write("\n".join(book_lines))


def izm (path):
    print("CПРАВОЧНИК")
    with open(path, "r") as data:
        book = data.read()
        print(book)
    print()
    
    index = int(input("Введите номер строки для изменения: ")) - 1
    book_lines = book.split("\n")
    book_lines[index]  = str(input("Новые данные: "))
    with open(path, "w", encoding='utf-8') as data:
        data.write("\n".join(book_lines))