filename = 'examples/guest.txt'
name = input('Введите ваше имя: ')

with open(filename, 'a', encoding='utf-8') as file_object:
    file_object.write(f'{name.title()}\n')
