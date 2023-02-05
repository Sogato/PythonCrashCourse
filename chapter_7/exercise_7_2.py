places = input('На сколько мест вы хотите забронировать столик?\n')
places = int(places)

if places == 8:
    print('Извините, свободных мест нет.')
else:
    print('Столик забронирован.')
