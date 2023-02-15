filename_cats = 'examples/cats.txt'
filename_dogs = 'examples/dogs.txt'

try:
    with open(filename_cats, encoding='utf-8') as f:
        cats = f.readlines()
except FileNotFoundError:
    pass
else:
    for cat in cats:
        print(cat.rstrip())
print()

try:
    with open(filename_dogs, encoding='utf-8') as f:
        dogs = f.readlines()
except FileNotFoundError:
    pass
else:
    for dog in dogs:
        print(dog.rstrip())
