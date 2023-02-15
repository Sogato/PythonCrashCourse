import json


def get_num():
    filename = 'examples/favorite_num.json'
    try:
        with open(filename) as f:
            favorite_num = json.load(f)
        return favorite_num

    except FileNotFoundError:
        return None


def set_num():
    filename = 'examples/favorite_num.json'
    favorite_num = input('Какое ваше любимое число? ')
    try:
        int(favorite_num)

    except ValueError:
        print('Это не число.')

    else:
        with open(filename, 'w') as f:
            json.dump(favorite_num, f)


def main():
    """Программа запоминает и выводит любимое число пользователя"""
    favorite_num = get_num()

    if favorite_num is None:
        set_num()
    else:
        print(f'Ваше любимое число: {favorite_num}')


main()
