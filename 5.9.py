# Без пользователей: добавьте в hello_admin.py команду if, которая проверит, что список пользователей не пуст.
# • Если список пуст, выведите сообщение «We need to ind some users!».
# • Удалите из списка все имена пользователей и убедитесь в том, что программа выводит правильное сообщение.

users = ['John', 'Jane', 'Admin', 'Mike', 'Max']
if users:
    for user in users:
        if user.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again')
else:
    print('We need to ind some users!')
