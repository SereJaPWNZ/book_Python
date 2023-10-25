# Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра вызовите для каждого экземпляра метод describe_restaurant().

class Restaurant():
    '''модель ресторана'''

    def __init__(self, cuisine_type):
        '''Инициация атрибута типом кухни'''
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Вывод описания ресторана'''
        print(f'Тип кухни - {self.cuisine_type}.')

restaurant_1 = Restaurant('Японская')
restaurant_2 = Restaurant('Русская')
restaurant_3 = Restaurant('Европейская')

print(f'Наши кухни: {restaurant_1.cuisine_type.title()}, {restaurant_2.cuisine_type.title()}, {restaurant_3.cuisine_type.title()}')