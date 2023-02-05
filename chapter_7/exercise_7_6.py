message = 'Для выхода введите "Выйти"'
message += '\nВведите ваш возраст: '
active = 0

while True:
    age = input(message)

    if age == 'Выйти':
        break

    age = int(age)

    if age < 3:
        print('Билет беспланый.', end=' ')
    elif 3 <= age < 12:
        print('Билет стоит 500 рублей.', end=' ')
    elif 12 <= age:
        print('Билет стоит 750 рублей.', end=' ')

    active += 1
    print(f'Номер билета: {active}\n')
