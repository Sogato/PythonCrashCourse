class User:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
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


class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения",
                           "разрешено удалять пользователей",
                           "разрешено банить пользователей",
                           ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
