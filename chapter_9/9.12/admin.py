'''импортирование родительского класса'''
from user1 import User

class Admin(User):
    '''Учетный профиль администратора'''

    def __init__(self, first_name, last_name, birthday, have_pets, privileges=None):
        '''Инициализируем атрибуты родителя. Добавляем атрибут привилегий'''
        super().__init__(first_name, last_name, birthday, have_pets)
        privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']
        self.privileges = privileges
