human_0 = {
    'first_name': 'Томас',
    'last_name': 'Шелби',
    'age': 32,
    'city': 'Улан-Удэ',
}
human_1 = {
    'first_name': 'Паровозик',
    'last_name': 'Томас',
    'age': 104,
    'city': 'Улан-Батор',
}
human_2 = {
    'first_name': 'Хан',
    'last_name': 'Милос',
    'age': 16,
    'city': 'Улан-Вагон',
}

people = [human_0, human_1, human_2]

for human in people:
    print(f'Имя: {human["first_name"]} {human["last_name"]}')
    print(f'Возраст: {human["age"]}')
    print(f'Город: {human["city"]}\n')
