def build_sandwich(*args):
    print('Сэндвич состоит из:')
    for arg in args:
        print(f'\t-{arg}')
    print()


build_sandwich('Булочка')
build_sandwich('Булочка', 'Котлета')
build_sandwich('Булочка', 'Котлета', 'Помидор', 'Огурец', 'Соус')
