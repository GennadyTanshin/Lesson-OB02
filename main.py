class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'Пользователь'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def __str__(self):
        return f'ID: {self.__user_id}, Имя: {self.__name}, Уровень доступа: {self.__access_level}'


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'Админ'
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} удалён.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        for user in self.__users:
            print(user)

# Пример использования
admin = Admin(1, "Злой админ Сеня")
user1 = User(2, "Бедный юзер Петя")
user2 = User(3, "Бедный юзер Коля")

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(2)
admin.list_users()
