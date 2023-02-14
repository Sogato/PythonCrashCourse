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


restaurant_1 = Restaurant('Оливейра', 'грузинская')
restaurant_2 = Restaurant('Гинза', 'японская')
restaurant_3 = Restaurant('Вкусно и точка', 'западная')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
