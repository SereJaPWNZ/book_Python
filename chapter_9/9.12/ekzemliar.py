'''импортирование родительских классов'''
from admin import Admin
from privileges import Privileges

Admin = Admin('Andrey', 'Alikov', '25.08.1996', True)
privileges_Admin = Privileges('Все права')
print(privileges_Admin.see_privileges())
