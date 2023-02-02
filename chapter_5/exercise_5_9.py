users = []

if users:
    for user in users:
        if user != 'admin':
            print(f'Привет {user}, рад видеть тебя вновь.')
        else:
            print(f'Привет {user}, за работу.')
else:
    print('Пользователей не найдено.')
