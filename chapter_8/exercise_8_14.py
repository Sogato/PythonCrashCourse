def build_car(brand, name, **kwargs):
    kwargs['brand'] = brand
    kwargs['name'] = name
    return kwargs


car = build_car('BMW', 'X6', color='black', tow_package=True)
print(car)
