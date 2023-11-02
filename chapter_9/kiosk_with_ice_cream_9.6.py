# киоск с мороженым — особая разновидность ресторана. 
# Напишите класс IceCreamStand, наследующий от класса
# Restaurant из упражнения 9.1 (с. 175) или
# упражнения 9.4 (с. 180). Подойдет любая версия класса; просто выберите ту, которая вам больше нравится. Добавьте атрибут 
# с именем flavors для хранения списка сортов мороженого
# Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.

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


class IceCreamStand(Restaurant):
    '''Представляет аспекты ресторана, специфические для киоска с мороженным.'''

    def __init__(self, restaurant_name, cuisine_type, flavors):
        '''Инициализируем атрибуты класса родителя. Добавляем атрибут со списком хранимых сортов мороженного'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def output_of_the_list_of_ice_cream_varieties(self):
        '''Вывод списка с сортами мороженного'''
        return self.flavors

restaurant = IceCreamStand('Anime', 'Все типы', ('Sort- A', 'Sort - B', 'Sort - C'))
print(restaurant.output_of_the_list_of_ice_cream_varieties())
