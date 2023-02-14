class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Ресторан: {self.restaurant_name}')
        print(f'Тип кухни: {self.cuisine_type}')
        print(f'Кол-во обслуженных поситителей: {self.number_served}')
        print()

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

    @staticmethod
    def open_restaurant():
        print('Ресторан открыт!')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream = IceCreamStand("Незабудка", '', ["Ваниль", "Шоколад", "Кокос"])
ice_cream.print_flavors()
