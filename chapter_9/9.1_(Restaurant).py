# создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.

class Restaurant():
    '''модель ресторана'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Инициация атрибутов названия ресторана и его типа кухни'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Вывод описания ресторана'''
        print(f'Тип кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        '''Вывод названия ресторана'''
        print(f'{self.restaurant_name} - ресторан открыт!')

    
my_restaurant = Restaurant('Volgograd', 'Russian')

print(f'Название ресторана - {my_restaurant.restaurant_name.title()}.')
print(f'Тип кухни ресторана - {my_restaurant.cuisine_type.title()}.')

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()