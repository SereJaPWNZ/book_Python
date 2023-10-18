# Города: напишите функцию describe_city(), которая получает названия города и страны. Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»). Задайте параметру страны значение по умолчанию. Вызовите свою функцию для трех разных городов, по крайней мере один из которых не находится в стране по умолчанию.

def describe_city(city_name, country='Russia'):
    print(f'{city_name} is in {country}')


describe_city('Volgograd')
describe_city('Moscow')
describe_city('New York', 'USA')
