class User:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self. age = age
        self.email = email
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f'Имя: {self.first_name}')
        print(f'Фимилия: {self.last_name}')
        print(f'Возраст: {self.age}')
        print(f'Email: {self.email}')
        print(f'Кол-во входов: {self.login_attempts}')
        print()

    def greet_user(self):
        print(f'Привет {self.first_name} {self.last_name}!')
        print()


user = User('Андрей', 'Волк', '18', 'ayf@gmail.com')

user.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()

user.reset_login_attempts()
user.describe_user()
