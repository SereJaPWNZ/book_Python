# Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9.3(с. 175). 
# Напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1.
# Напишите другой метод с именем reset_login_attempts(),
# обнуляющий значение login_attempts.
# Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.
# Выведите значение login_attempts, чтобы убедиться в том,
# что значение было изменено правильно, а затем вызовите reset_login_attempts().
# Снова выведите login_attempts и убедитесь в том, что значение обнулилось.

class User():
    '''Обычный пользователь'''

    def __init__(self, first_name, last_name, birthday, have_pets):
        '''Инициализируем атрибуты имени и фамилии, даты рождения, наличия животного'''
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.have_pets = have_pets
        self.login_attempts = 0

    def describe_user(self):
        '''Вывод сводки с информацией о пользователе'''
        print(f'Имя: {self.first_name.title()}, Фамилия: {self.last_name.title()}, Дата рождения: {self.birthday}, Наличие питомца: {self.have_pets}')

    def greet_user(self):
        '''Вывод персональных приветствий'''
        print(
            f'Добро пожаловать, {self.first_name.title()} {self.last_name.title()}!')
        
    def increment_login_attempts(self):
        '''Увеличение счетчика количества попыток входа на 1'''
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        '''Сброс количества попыток входа'''
        self.login_attempts = 0
        return self.login_attempts

person_1 = User(first_name='andrey', last_name='Smith',
                birthday='12.05.1990', have_pets='True')

# person_2 = User(first_name='John', last_name='Doe',
#                 birthday='23.10.2000', have_pets='False')

# person_3 = User(first_name='Jane', last_name='Doe',
#                 birthday='01.01.2021', have_pets='True')

person_1.increment_login_attempts()
person_1.increment_login_attempts()
person_1.increment_login_attempts()
print(person_1.login_attempts)
person_1.reset_login_attempts()
print(person_1.login_attempts)