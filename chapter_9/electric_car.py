'''Набор классов для представления электромобилей.'''
from car import Car

class Battery():
    '''Простая модель аккумулятора'''

    def __init__(self, battery_size=75):
        '''Инициализируем атрибут аккумулятора'''
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        power_battery = f'This car has a {self.battery_size} -kWh battery.'
        return power_battery
    def get_range_iterable(self):
        '''Выводит приблизительный запас хода для аккумулятора'''
        if self.battery_size == 75:
            stock = 260
        elif self.battery_size == 100:
            stock = 315
        print(f"This car can go about {stock} miles on a full charge.")


class ElectricCar(Car):
    '''Представляет аспекты машины, специфические для электромобилей.'''
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.'''
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'x', 2013)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
my_tesla.battery.get_range_iterable()
