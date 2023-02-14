from user import User


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
