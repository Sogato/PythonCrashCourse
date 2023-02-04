favorite_places = {
    'Пирамиды': ['Вася', 'Аня'],
    'Реки': ['Аня', 'Вера'],
    'Горы': ['Коля', 'Аня', 'Вася'],
}

frieds = ['Аня', 'Вася', 'Коля', 'Вера']

for fried in frieds:
    print(f'Любимые места {fried} - это ', end='')
    for key, value in favorite_places.items():
        if fried in value:
            print(f'{key}', end=' ')
    print()
