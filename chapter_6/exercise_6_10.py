favorite_numbers = {
    'Никита': [69, 656],
    'Вася': [13, 25, 1],
    'Коля': [20],
    'Анатолий': [3, 0],
    'Пётр': [25, 12, 158, 322],
}

for key, value in favorite_numbers.items():
    print(f'Любимые число {key}: ', end='')
    for number in value:
        print(number, end=' ')
    print()
