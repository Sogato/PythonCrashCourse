stesha = {
    'type': 'Кошка',
    'master_name': 'Андрей',
}
lycia = {
    'type': 'Собака',
    'master_name': 'Таня',
}
bacsik = {
    'type': 'Кот',
    'master_name': 'Неизвестно',
}

pets = [stesha, lycia, bacsik]

for pet in pets:
    print(f'Тип животного: {pet["type"]}')
    print(f'Имя хозяина: {pet["master_name"]}\n')
