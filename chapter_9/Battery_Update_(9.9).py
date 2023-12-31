# Обновление аккумулятора: используйте окончательную версию
# программы electric_car.py из этого раздела.
# Добавьте в класс Battery метод с именем upgrade_battery().
# Этот метод должен проверять размер аккумулятора и
# устанавливать мощность равной 100, если она имеет другое
# значение. Создайте экземпляр электромобиля с аккумулятором
# по умолчанию, вызовите get_range(), а затем вызовите
# get_range() во второй раз после вызова upgrade_battery().
# Убедитесь в том, что запас хода увеличился.

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Возвращаем отформатированное описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
     
    def read_odometer(self):
        '''Выводит пробег машины'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        '''Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''Увеличение показателей одометра с заданным приращением.'''
        self.odometer_reading += miles

class Battery():
    '''Простая модель аккумулятора'''

    def __init__(self, battery_size=75):
        '''Инициализируем атрибут аккумулятора'''
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        power = f'This car has a {self.battery_size} -kWh battery.'
        return power
    
    def get_range_iterable(self):
        '''Выводит приблизительный запас хода для аккумулятора'''
        if self.battery_size == 75:
            stock = 260
        elif self.battery_size == 100:
            stock = 315
        print(f"This car can go about {stock} miles on a full charge.")

    def upgrade_battery(self):
        '''Проверяет размер аккумулятора и устанавливает мощность равной 100'''
        if self.battery_size < 100:
            self.battery_size = 100
        return self.battery_size


class ElectricCar(Car):
    '''Представляет аспекты машины, специфические для электромобилей.'''
    
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.'''
        super().__init__(make, model, year)
        self.battery = Battery()

basic_electric_car = ElectricCar('Mersedes', 'EQS', 2023)

basic_electric_car.battery.get_range_iterable()
basic_electric_car.battery.upgrade_battery()
basic_electric_car.battery.get_range_iterable()