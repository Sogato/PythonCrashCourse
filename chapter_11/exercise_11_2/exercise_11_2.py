def set_address(country, city, population=0):
    if population == 0:
        address = f'{country}, {city}'
    else:
        address = f'{country}, {city} - население {population}'
    return address.title()
