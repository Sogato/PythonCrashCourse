human = {
    'first_name': 'Томас',
    'last_name': 'Шелби',
    'age': 32,
    'city': 'Улан-Удэ',
}

testGet = human.get('Test', 'Такого ключа не сущетсвует')
print(human['first_name'], human['last_name'], human['age'], human['city'], testGet)
