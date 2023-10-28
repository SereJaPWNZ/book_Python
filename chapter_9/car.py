'''Создаем класс автомобили, после чего форматируем полученные экземпляры и выводим текст'''


class Car():
    '''Типовая модель автомобиля'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Возвращаем отформатированное описание'''
        long_name = f'{self.make}, {self.model}, {self.year}'
        return long_name.title()

    def read__odometer(self):
        '''Выводит пробег машины'''
        print(f'{self.odometer_reading}')

    def update_odometr(self, mileage):
        '''Устанавливает на одометре заданное значение. При попытке обратной подкрутки изменение отклоняется.'''
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''Увеличение показателей одометра с заданным приращением.'''
        self.odometer_reading += miles
        return self.odometer_reading


# my_new_car = Car('suzuki', 'x', 1996)
# my_new_car.odometer_reading = 39
# my_new_car.update_odometr(40)
# my_new_car.read__odometer()
my_used_car = Car('suzuki', 'x', 1996)
my_used_car.update_odometr(3000)
my_used_car.increment_odometer(1000)
my_used_car.read__odometer()
my_used_car.update_odometr(7000)
my_used_car.read__odometer()