filename_cats = 'examples/cats.txt'
filename_dogs = 'examples/dogs.txt'

try:
    with open(filename_cats, encoding='utf-8') as file_object:
        cats = file_object.readlines()
except FileNotFoundError:
    print(f'Файл "{filename_cats}" не найден.')
else:
    for cat in cats:
        print(cat.rstrip())
print()

try:
    with open(filename_dogs, encoding='utf-8') as file_object:
        dogs = file_object.readlines()
except FileNotFoundError:
    print(f'Файл "{filename_dogs}" не найден.')
else:
    for dog in dogs:
        print(dog.rstrip())
