class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Ресторан: {self.restaurant_name}')
        print(f'Тип кухни: {self.cuisine_type}')
        print()

    @staticmethod
    def open_restaurant():
        print('Ресторан открыт!')


restaurant = Restaurant('Оливейра', 'грузинская')
restaurant.describe_restaurant()
restaurant.open_restaurant()
