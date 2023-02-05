number = input('Введите число: ')
number = int(number)

if number % 10 == 0:
    print(f'Число {number} кратно 10.')
else:
    print(f'Число {number} не кратно 10.')
