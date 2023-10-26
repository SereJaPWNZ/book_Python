# Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя.
# Напишите метод describe_user(), который выводит сводку с информацией о пользователе.
# Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
# Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.

class User():
    '''Обычный пользователь'''

    def __init__(self, first_name, last_name, birthday, have_pets):
        '''Инициализируем атрибуты имени и фамилии, даты рождения, наличия животного'''
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.have_pets = have_pets

    def describe_user(self):
        '''Вывод сводки с информацией о пользователе'''
        print(f'Имя: {self.first_name.title()}, Фамилия: {self.last_name.title()}, Дата рождения: {self.birthday}, Наличие питомца: {self.have_pets}')

    def greet_user(self):
        '''Вывод персональных приветствий'''
        print(
            f'Добро пожаловать, {self.first_name.title()} {self.last_name.title()}!')


person_1 = User(first_name='andrey', last_name='Smith',
                birthday='12.05.1990', have_pets='True')

person_2 = User(first_name='John', last_name='Doe',
                birthday='23.10.2000', have_pets='False')

person_3 = User(first_name='Jane', last_name='Doe',
                birthday='01.01.2021', have_pets='True')

person_1.describe_user()
person_2.describe_user()
person_3.describe_user()

person_1.greet_user()
person_2.greet_user()
person_3.greet_user()
