import json

filename = '../examples/favorite_num.json'

favorite_num = input('Какое ваше любимое число? ')
with open(filename, 'w') as f:
    json.dump(favorite_num, f)
