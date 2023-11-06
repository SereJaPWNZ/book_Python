"""Класс для представления машин с бензиновым и электродвигателем."""
class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализация атрибутов аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            stock = 260
        elif self.battery_size == 100:
            stock = 315
        print(f"This car can go about {stock} miles on a full charge.")

class ElectricCar(Car):
    """Представляет аспекты машины, специфические 
    для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические
        для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

# ------------------------------------------
# Old version
# '''Создаем класс автомобили, после чего форматируем полученные экземпляры и выводим текст'''

# class Car():
#     '''Типовая модель автомобиля'''

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         '''Возвращаем отформатированное описание'''
#         long_name = f'{self.make}, {self.model}, {self.year}'
#         return long_name.title()

#     def read__odometer(self):
#         '''Выводит пробег машины'''
#         print(f'{self.odometer_reading}')

#     def update_odometr(self, mileage):
#         '''Устанавливает на одометре заданное значение.
# При попытке обратной подкрутки изменение отклоняется.'''
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         '''Увеличение показателей одометра с заданным приращением.'''
#         self.odometer_reading += miles
#         return self.odometer_reading


# my_new_car = Car('suzuki', 'x', 1996)
# my_new_car.odometer_reading = 39
# my_new_car.update_odometr(40)
# my_new_car.read__odometer()
# my_used_car = Car('suzuki', 'x', 1996)
# my_used_car.update_odometr(3000)
# my_used_car.increment_odometer(1000)
# my_used_car.read__odometer()
# my_used_car.update_odometr(7000)
# my_used_car.read__odometer()
