# администратор — особая разновидность пользователя
# Напишите класс с именем Admin, наследующий от класса User из
# упражнения 9.3 или упражнения 9.5(с. 180).
# Добавьте атрибут privileges для хранения списка строк вида
# "разрешено добавлять сообщения", "разрешено удалять
# пользователей", "разрешено банить пользователей" и т. д.
# Напишите метод show_privileges() для вывода набора привилегий
# администратора. Создайте экземпляр Admin и вызовите свой метод.

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
        
class Admin(User):
    '''Учетный профиль администратора'''

    def __init__(self, first_name, last_name, birthday, have_pets, privileges=None):
        '''Инициализируем атрибуты родителя. Добавляем атрибут привилегий'''
        super().__init__(first_name, last_name, birthday, have_pets)
        privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']
        self.privileges = privileges

    def show_privileges(self):
        '''Возвращает привилегии'''
        return self.privileges
    
admin = Admin('Admin', '-', '23.02.1997', False)
print(admin.show_privileges())
