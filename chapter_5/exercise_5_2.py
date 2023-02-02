print('Проверка равенства и неравенства строк.')
car = 'subaru'
print(car == 'subaru')
print(car != 'subaru')

print('\nПроверки с использованием функции lower().')
car = 'Subaru'
print(car.lower() == 'subaru')
print(car.lower() != 'subaru')

print('\nЧисловые проверки равенства и неравенства.')
number = 8
print(number == 8)
print(number != 8)
print(number > 8)
print(number >= 8)
print(number < 8)
print(number <= 8)

print('\nПроверки с ключевым словом and и or.')
print(number >= 8 and number != 0)
print(number <= 8 or number == 12)

numbers = [2, 4, 5, 0]
print('\nПроверка вхождения элемента в список.')
print(2 in numbers)

print('\nПроверка отсутствия элемента в списке')
print(1 not in numbers)
