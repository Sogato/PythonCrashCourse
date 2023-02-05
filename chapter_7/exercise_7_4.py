message = 'Для выхода введите "Выйти"'
message += '\nВведите дополнение для пиццы: '

while True:
    topping = input(message)
    if topping == 'Выйти':
        break
    print(f'{topping.title()} включено в заказ.\n')
