# Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут number_served со значением по умолчанию 0; он представляет количество обслуженных посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served, потом измените и выведите снова. Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей. Вызовите метод с новым числом, снова выведите значение. Добавьте метод с именем increment_number_served(), который увеличивает количество обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов, — скажем, за один день.

class Restaurant():
    '''модель ресторана'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Инициация атрибутов названия ресторана и его типа кухни'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # количество обслуженных посетителей

    def describe_restaurant(self):
        '''Вывод описания ресторана'''
        print(f'Ресторан - {self.restaurant_name} c типом кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        '''Вывод сообщения об открытии ресторана'''
        print(f'{self.restaurant_name} - ресторан открыт!')

    def set_number_served(self, new_number_served):
        '''Выставление количества обслуженных посетителей'''
        self.number_served = new_number_served
        return self.number_served
    
    def increment_number_served(self, increase_number):
        '''Увеличиваем количество обслуженных посетителей на заданную величину'''
        self.number_served += increase_number

restaurant = Restaurant('Volgograd', 'Russian')
print(restaurant.number_served)
restaurant.number_served = 15
print(restaurant.number_served)
restaurant.set_number_served(30)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.number_served)
