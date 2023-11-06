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