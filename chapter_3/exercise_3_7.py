guests = ['Томас Шелби', 'Кристиан Бейл', 'Ханс Циммер']
print(f'Привет {guests[0]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[1]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[2]}, приглашаю тебя на обед завтра вечером.')

print(f'\nПохоже, {guests[2]} не сможет прийти.\n')
guests[2] = 'Скала Джонсон'

print(f'Привет {guests[0]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[1]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[2]}, приглашаю тебя на обед завтра вечером.')

print(f'\nПохоже, на обед можно позвать больше гостей.\n')
guests.insert(0, 'Барак Обама')
guests.insert(3, 'Леди Баг')
guests.append('Рикардо Милос')

print(f'Привет {guests[0]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[1]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[2]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[3]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[4]}, приглашаю тебя на обед завтра вечером.')
print(f'Привет {guests[5]}, приглашаю тебя на обед завтра вечером.')

print(f'\nУпс, места хватит всего на двоих.\n')
print(f'Извини {guests.pop(-1)}, но для тебя нет места за моим столом.')
print(f'Извини {guests.pop(-1)}, но для тебя нет места за моим столом.')
print(f'Извини {guests.pop(-1)}, но для тебя нет места за моим столом.')
print(f'Извини {guests.pop(-1)}, но для тебя нет места за моим столом.\n')

print(f'Привет {guests[0]}, хотел напомнить что мое приглашение еще в силе!')
print(f'Привет {guests[1]}, хотел напомнить что мое приглашение еще в силе!')

del guests[0]
del guests[1]

print(guests)
