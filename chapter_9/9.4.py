# Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут number_served со значением по умолчанию 0; он представляет количество обслуженных посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served, потом измените и выведите снова. Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей. Вызовите метод с новым числом, снова выведите значение. Добавьте метод с именем increment_number_served(), который увеличивает количество обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов, — скажем, за один день.

class Restaurant():
    '''модель ресторана'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Инициация атрибутов названия ресторана и его типа кухни'''
        self.restaurant_name = restaurant_name  # инициализация имени ресторана
        self.cuisine_type = cuisine_type  # инициализация типа кухни
        self.number_served = 0  # инициализация количества обслуженных посетителей

    def describe_restaurant(self):
        '''Вывод описания ресторана'''
        print(f'Тип кухни - {self.cuisine_type}.')

    def open_restaurant(self):
        '''Вывод названия ресторана'''
        print(f'{self.restaurant_name} - ресторан открыт!')

    def read_number_served(self):
        '''Вывод количества обслуживаемых клиентов'''
        return self.number_served
    
    def set_number_served(self, number_visitors):
        '''Выставление количества обслуженных посетителей'''
        self.number_served = number_visitors
        return self.number_served

    def increment_number_served(self, increment_number):
        '''Увеличивание количество обслуженных посетителей на заданную величину.'''
        self.number_served += increment_number
        return self.number_served

restaurant = Restaurant('Volgograd', 'Russian')
print(restaurant.read_number_served())
restaurant.number_served = 10
print(restaurant.read_number_served())
restaurant.set_number_served(30)
print(restaurant.read_number_served())
restaurant.increment_number_served(50)
print(restaurant.read_number_served())
