# Hello Admin: создайте список из пяти и более имен пользователей, включающий имя 'admin'. Представьте, что вы пишете код, который выводит приветственное сообщение для каждого пользователя после его входа на сайт. Переберите элементы списка и выведите сообщение для каждого пользователя:
# • Для пользователя с именем 'admin’ выведите особое сообщение — например, «Hello admin, would you like to see a status report?».
# • В остальных случаях выводите универсальное приветствие — например, «Hello Jaden, thank you for logging in again».

users = ['John', 'Jane', 'Admin', 'Mike', 'Max']
for user in users:
    if user.lower() == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again')
