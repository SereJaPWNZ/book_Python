class Dog():
    '''Простая модель собаки'''

    def __init__(self, name, age):
        '''Инициализируем атрибуты name, age'''
        self.name = name
        self.age = age

    def sit(self):
        '''Собака садиться по команде'''
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        '''Собака перекатывается по команде'''
        print(f'{self.name.title()} rolled over!')


my_dog = Dog('willi', 26)
you_dog = Dog('Tiko', 10)

print(f'My dog name is {my_dog.name.title()}.')
print(f'My dog is {my_dog.age} years old.')

my_dog.sit()
my_dog.roll_over()
you_dog.sit()