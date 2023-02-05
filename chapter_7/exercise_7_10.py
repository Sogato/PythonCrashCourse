vacationSurvey = {}

surveyActive = True

while surveyActive:
    name = input('Добрый день, как вас зовут? ')
    location = input('Где бы вы хотели провести отпуск? ')
    vacationSurvey[name] = location

    choice = input('Хотите ли вы продолжить опрос? (да/нет) ')
    if choice.lower() == 'нет':
        surveyActive = False
    print()

for name, location in vacationSurvey.items():
    print(f'{name.title()} хочет провести отпуск {location.lower()}')
