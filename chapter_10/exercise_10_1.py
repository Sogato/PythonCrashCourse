filename = 'examples/todolist.txt'

with open(filename, encoding='utf-8') as file_object:
    content = file_object.read()  # Чтение всего файла
    print(content)

with open(filename, encoding='utf-8') as file_object:
    for line in file_object:  # Чтение файла по строкам
        print(line.rstrip())
    print()

with open(filename, encoding='utf-8') as file_object:
    lines = file_object.readlines()  # Сохранение файла в массив строк

for line in lines:
    print(line.rstrip())
