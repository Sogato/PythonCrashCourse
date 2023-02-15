filename = 'examples/guest_book.txt'

while True:
    name = input('Введите "Выход" чтобы выйти.\n'
                 'Введите ваше имя: ')

    if name.lower() == 'выход':
        break

    message = f'Привет {name.title()}!\n'
    print(message)

    with open(filename, 'a', encoding='utf-8') as file_object:
        file_object.write(message)
