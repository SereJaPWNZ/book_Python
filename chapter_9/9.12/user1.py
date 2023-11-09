'''Класс для представления свойств пользователя'''
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
