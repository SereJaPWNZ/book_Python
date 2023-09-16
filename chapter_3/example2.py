motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# Присоединение элементов в конец списка

motorcycles.append('ducati')
print(motorcycles)

# Вставка элементов в список
motorcycles.insert(2, 'fiat')
print(motorcycles)

# Удаление элемента с использованием команды del
del motorcycles[2]
print(motorcycles)

# Удаление элемента с использованием метода pop()
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

# Извлечение элементов из произвольной позиции списка

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Удаление элементов по значению

motorcycles.remove('suzuki')
print(motorcycles)
