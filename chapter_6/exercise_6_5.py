rivers = {
    'Томь': 'Россия',
    'Нил': 'Египет',
    'Амазонка': 'Бразилия',
}

for key, value in rivers.items():
    print(f'Река {key} протекает через страну {value}')

print('\nРеки: ', end='')
for key in rivers.keys():
    print(key, end=' ')

print('\nСтраны: ', end='')
for value in rivers.values():
    print(value, end=' ')
