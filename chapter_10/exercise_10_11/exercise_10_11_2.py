import json

filename = '../examples/favorite_num.json'

with open(filename) as f:
    print(f'Ваше любимое число: {json.load(f)}')
