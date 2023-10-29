# создайте класс с именем Restaurant.
#  Метод __init__() класса Restaurant должен содержать два атрибута: 
#  restaurant_name и cuisine_type. 
#  Создайте метод describe_restaurant(), который выводит два атрибута, 
#  и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт. 
#  Создайте на основе своего класса экземпляр с именем restaurant. 
#  Выведите два атрибута по отдельности, затем вызовите оба метода.


class Restaurant():
    '''модель ресторана'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Инициация атрибутов названия ресторана и его типа кухни'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Вывод описания ресторана'''
        print(f'Ресторан - {self.restaurant_name} c типом кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        '''Вывод сообщения об открытии ресторана'''
        print(f'{self.restaurant_name} - ресторан открыт!')

restaurant = Restaurant('Volgograd', 'Russian')

name_restaurant = restaurant.restaurant_name
print(name_restaurant)
restaurant_type = restaurant.cuisine_type
print(restaurant_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
