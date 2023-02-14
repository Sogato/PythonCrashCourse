from secrets import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

number_1 = choice(numbers)
number_2 = choice(numbers)
number_3 = choice(numbers)
number_4 = choice(numbers)
winner = f'{number_1} {number_2} {number_3} {number_4}'

print(f'Счастливый билет: {winner}', end='\n')

my_ticket = ''
counter = 0
while my_ticket != winner:

    counter += 1
    number_1 = choice(numbers)
    number_2 = choice(numbers)
    number_3 = choice(numbers)
    number_4 = choice(numbers)
    my_ticket = f'{number_1} {number_2} {number_3} {number_4}'

    print(f'Мой билет: {my_ticket} Попытка №{counter}')

print(f'Счастливый билет: {winner}')
