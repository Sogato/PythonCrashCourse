cities = {
    'Прокопьевск': {
        'country': 'Россия',
        'population': '200000',
        'fact': 'Угольный город',
        },
    'Томск': {
        'country': 'Россия',
        'population': '350000',
        'fact': 'Студенческий город',
        },
    'Новосибирск': {
        'country': 'Россия',
        'population': '1000000',
        'fact': 'Столица Сибири',
        },
}

for city, info in cities.items():
    print(f'Название города {city}')
    print(f'\tСтрана: {info["country"]}')
    print(f'\tНаселение: {info["population"]}')
    print(f'\tИнтерестный факт: {info["fact"]}', end='\n\n')
