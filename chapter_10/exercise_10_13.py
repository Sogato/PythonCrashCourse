import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'examples/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("Как тебя зовут? ")
    filename = 'examples/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        while True:
            check = input(f'Правильно ли введено имя пользователя? {username} (y/n): ')
            if check.lower() == 'y':
                print(f"Добро пожаловать, {username}!")
                break
            elif check.lower() == 'n':
                username = get_new_username()
                print(f"Я запомню тебя, {username}!")
                break
            else:
                print('Неккоректный ввод.')
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
