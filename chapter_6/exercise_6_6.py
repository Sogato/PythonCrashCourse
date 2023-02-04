favorite_numbers = {
    'Никита': 69,
    'Вася': 13,
    'Коля': 20,
    'Анатолий': 3,
    'Пётр': 25,
}
friends = ['Никита', 'Вера', 'Коля', 'Аня']

for friend in friends:
    print(f'Привет {friend}')

    if friend in favorite_numbers.keys():
        print('\tСпасибо за участие в опросе.')
    else:
        print('\tНе желаешь принять участие в опросе?')
