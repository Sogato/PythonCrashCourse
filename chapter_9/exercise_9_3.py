class User:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self. age = age
        self.email = email

    def describe_user(self):
        print(f'Имя: {self.first_name}')
        print(f'Фимилия: {self.last_name}')
        print(f'Возраст: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Привет {self.first_name} {self.last_name}!')
        print()


user_1 = User('Аюр', 'Чингисханов', '20', 'vfdsgdbgf@gmail.com')
user_2 = User('Максим', 'Шелби', '26', 'pudgara@gmail.com')
user_3 = User('Андрей', 'Волк', '18', 'ayf@gmail.com')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
