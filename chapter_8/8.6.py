# Названия городов: напишите функцию city_country(), которая получает название города и страну. Функция должна возвращать строку в формате "Santiago, Chile". Вызовите свою функцию по крайней мере для трех пар «город — страна» и выведите возвращенное значение.

def city_country(city_name, country):
    '''Возвращает название города и страны в отформатированном виде'''
    full_adress = f'{city_name}, {country}'
    return full_adress.title()


while True:
    print("\nenter 'q' at any time to quit")
    city_name = input('Введите название города: ')
    if city_name.lower() == 'q':
        break
    country = input('Введите название страны: ')
    if country.lower() == 'q':
        break
    elif len(city_name) > 0 and len(country) > 0:
        format_adress = city_country(city_name, country)
    elif len(city_name) > 0:
        format_adress = city_country(city_name, 'russia')
    elif len(country) > 0:
        format_adress = city_country('volgograd', 'russia')
    else:
        print('Значения названия города и страны не заданы, попробуйте еще раз!')
        break
    print(format_adress)
