countries = ['Россия', 'Япония', 'Германия', 'Сербия', 'Вьетнам']

print('Исходный массив: ', countries)
print('Сортировка в алфавитном порядке: ', sorted(countries))  # Сортировка без изменения массива
print('Исходный массив: ', countries)

print('Сортировка в обратном алфавитном порядке: ', sorted(countries, reverse=True))  # Сортировка без изменения
# массива (обратная)
print('Исходный массив: ', countries)

countries.reverse()  # Обратная сортировка
print('Сортировка в обратном порядке: ', countries)
countries.reverse()
print('Исходный массив: ', countries)

countries.sort()  # Сортировка с изменением массива
print('Сортировка в алфавитном порядке: ', countries)
countries.sort(reverse=True) # Сортировка (обратная) с изменением массива
print('Сортировка в обратном алфавитном порядке: ', countries)
