# Человек: используйте словарь для сохранения информации об известном вам человеке.
# Сохраните имя, фамилию, возраст и город, в котором живет этот человек.
# Словарь должен содержать ключи с такими именами, как first_name, last_name, age и city.
# Выведите каждый фрагмент информации, хранящийся в словаре.

people = {'first_name': 'Sergey', 'last_name': 'Morkovkin',
          'age': 27, 'city': 'Volgograd'}

print(people.get('first_name', 'sorry'))
print(people.get('last_name', 'sorry'))
print(people.get('age', 'sorry'))
print(people.get('city', 'sorry'))
