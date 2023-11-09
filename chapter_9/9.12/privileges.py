'''Класс для представления привелегий пользователя'''
class Privileges():
    '''Привелегии'''
    def __init__(self, privileges=None):
        '''Инициализация атрибутов родителя'''
        self.privileges = privileges

    def see_privileges(self):
        '''Вывод привилегий'''
        return self.privileges
