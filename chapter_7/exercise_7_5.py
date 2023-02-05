message = 'Для выхода введите "Выйти"'
message += '\nВведите ваш возраст: '

while True:
    age = input(message)
    age = int(age)

    if age < 3:
        print('Билет беспланый.')
    elif 3 <= age < 12:
        print('Билет стоит 500 рублей.')
    elif 12 <= age:
        print('Билет стоит 750 рублей.')
    print()
