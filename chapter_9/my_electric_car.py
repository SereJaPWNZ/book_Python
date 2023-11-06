from car import ElectricCar

my_new_tesla = ElectricCar('audi', 'e-trone', 2024)
print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()