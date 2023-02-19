def make_album(artist_name, album_title, track_music=None):
    album = {
        'atrist': artist_name,
        'title': album_title,
        'track': track_music,
    }
    return album


while True:
    name = input('Введите имя артиста: ')
    title = input('Введите название альбома: ')
    track = input('Введите количество треков: ')

    dict_album = make_album(name, title, track)
    print(dict_album)

    choice = input('\nХотите продолжить? (да/нет): ')
    if choice.lower() == 'нет':
        break
