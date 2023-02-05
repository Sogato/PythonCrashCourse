sandwich_orders = ['Пастрома', 'Макчикен', 'Гамбургер', 'Пастрома', 'Чизбургер', 'Пастрома', 'Крабсбургер']
finished_sandwiches = []

print('Пастромы нет в наличии.\n')
while 'Пастрома' in sandwich_orders:
    sandwich_orders.remove('Пастрома')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Заказ {sandwich} готов!')
    finished_sandwiches.append(sandwich)

print('\nПриготовленные за день заказы: ', end='')
print(finished_sandwiches)
