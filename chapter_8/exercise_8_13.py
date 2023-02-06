def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('Андрей', 'Ферстапин', location='Токио', field='Програмист', age='21')
print(user_profile)
