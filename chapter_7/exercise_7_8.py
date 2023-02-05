sandwich_orders = ['Макчикен', 'Гамбургер', 'Чизбургер', 'Крабсбургер']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Заказ {sandwich} готов!')
    finished_sandwiches.append(sandwich)

print('\nПриготовленные за день заказы: ', end='')
print(finished_sandwiches)
