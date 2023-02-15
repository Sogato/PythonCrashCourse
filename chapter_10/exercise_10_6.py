print('Введите два числа для сложения.')
number_1 = input()
number_2 = input()

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
except ValueError:
    print('Символы нельзя складывать.')
else:
    print(f'{number_1} + {number_2} =', number_1 + number_2)
