while True:

    print('Введите два числа для сложения.')
    print('Для выхода введите "q".')

    number_1 = input()
    if number_1.lower() == 'q':
        break
    number_2 = input()
    if number_2.lower() == 'q':
        break

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print('Символы нельзя складывать.')
    else:
        print(f'{number_1} + {number_2} =', number_1 + number_2)
