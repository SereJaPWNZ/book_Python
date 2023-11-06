'''Набор классов для представления электромобилей.'''
from electric_car import ElectricCar as EC

my_new_tesla = EC('audi', 'e-trone', 2024)
print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range_iterable()
