# Реки: создайте словарь с названиями трех больших рек и стран, по которым протекает каждая река. Одна из возможных пар «ключ-значение» — 'nile': 'egypt'.
# • Используйте цикл для вывода сообщения с упоминанием реки и страны — например, «The Nile runs through Egypt».
# • Используйте цикл для вывода названия каждой реки, включенной в словарь.
# • Используйте цикл для вывода названия каждой страны, включенной в словарь.

rivers = {
    'nile': 'egypt',
    'yarkand': 'china',
    'yellowstone': 'united_states',
    'yamuna': 'india',
    'yap': 'papua_new_guinea',
    'yangtze': 'china',
    'yarowinsky': 'australia',
    'yasuni': 'bolivia',
    'wind': 'canada',
    'whitewater': 'zimbabwe'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

print('\nСписок рек:')
for river in rivers:
    print(river.title())

print('\nСписок стран:')
for country in rivers:
    print(country.title())
