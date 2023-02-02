pizzas = ['Пепперони', '4 Сыра', 'Пицца с ананасом']

friend_pizzas = pizzas[:]
pizzas.append('Пицца итальянская')
friend_pizzas.append('Пицца через бедность')

print('Мне нравится эти пиццы: ')
for pizza in pizzas:
    print(pizza)

print('\nМоему другу нравится эти пиццы: ')
for pizza in friend_pizzas:
    print(pizza)
