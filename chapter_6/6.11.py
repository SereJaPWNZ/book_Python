#  Города: создайте словарь с именем cities. Используйте названия трех городов в качестве ключей словаря. Создайте словарь с информацией о каждом городе; включите в него страну, в которой расположен город, примерную численность населения и один примечательный факт, относящийся к этому городу. Ключи словаря каждого города должны называться country, population и fact. Выведите название каждого города и всю сохраненную информацию о нем.

cities = {'London': {'country': 'United_Kingdom', 'population': 8679441, 'fact': 'The_London_Eye_is_a_ferris_wheel_located_in_London.'}, 'Paris': {'country': 'France',
                                                                                                                                                   'population': 2240885, 'fact': "Paris_is_the_capital_of_France."}, 'Berlin': {'country': 'Germany', 'population': 3622024, 'fact': 'Berlin_is_the_capital_of_Germany.'}}


for key, values in cities.items():
    print(f'\nНазвание города: {key}\nНазвание страны{values['country']}\nПопуляция{
          values['population']}\nИнтересный факт: {values['fact']}')
