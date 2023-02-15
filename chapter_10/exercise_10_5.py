filename = 'examples/survey.txt'

while True:
    answer = input('Введите "Выход" чтобы выйти.\n'
                 'Почему вам нравится Python: ')

    if answer.lower() == 'выход':
        break

    with open(filename, 'a', encoding='utf-8') as file_object:
        file_object.write(f'{answer}\n')
