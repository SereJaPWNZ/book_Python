'''Импортирована библиотека рандомных чисел для работы функции roll_die'''
from random import randint

class Die():
    '''Модель значений кубика'''
    def __init__(self, sides=6):
        '''Инициализируем атрибут sides'''
        self.sides = sides # грань куба

    def roll_die(self):
        '''Вывод рандомных чисел от 1 до количества граней на кубике'''
        number = randint(1, self.sides)
        return number
