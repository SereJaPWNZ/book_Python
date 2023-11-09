'''Набор класса для представления прав пользователя'''
from import_class import Privileges

Admin = Privileges('Full privileges')
print(Admin.see_privileges())
