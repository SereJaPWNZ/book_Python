# Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра вызовите для каждого экземпляра метод describe_restaurant().

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