def make_album(artist_name, album_title, track=None):
    album = {
        'atrist': artist_name,
        'title': album_title,
        'track': track,
    }
    return album


dict_album = make_album('Кот', 'Розы')
print(dict_album)
dict_album = make_album('Собака', 'Искры', 4)
print(dict_album)
dict_album = make_album('Рыба', 'Пламя')
print(dict_album)
