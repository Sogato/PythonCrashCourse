current_users = ['jgdg', 'oky', 'uza', 'admin', 'klown']
new_users = ['Admin', 'vasia', 'mumi', 'kLown', 'cake']

for user in new_users:
    if user.lower() in current_users:
        print(f'Такое имя ({user}) уже существует, выберите другое')
    elif user.lower() not in current_users:
        print(f'Имя {user} доступно.')
