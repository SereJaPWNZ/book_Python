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
        '''Обновление значений одометра'''
        self.odometer_reading = mileage


my_new_car = Car('suzuki', 'x', 1996)
my_new_car.odometer_reading = 39
my_new_car.update_odometr(90)
my_new_car.read__odometer()
