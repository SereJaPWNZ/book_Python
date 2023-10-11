# Расширение: примеры, с которыми мы работаем, стали достаточно сложными, и в них можно вносить разного рода усовершенствования. Воспользуйтесь одним из примеров этой главы и расширьте его: добавьте новые ключи и значения, измените контекст программы или улучшите форматирование вывода.

# Создайте пустой словарь и выведите его на экран.

empty_dict = dict()
print(empty_dict)

# Создайте словарь с некоторыми данными и выведите его на экран.

sex = {"Andrey": "male", "Anna": "female"}
print(sex)

# Получите значение определенного ключа из словаря и выведите его на экран.

print(sex['Andrey'])

# Удалите определенный ключ из словаря и проверьте, был ли он удален.

key = sex["Andrey"]
del sex["Andrey"]
print(sex)

if key in sex.keys():
    print('YES')
else:
    print('NO')

# Измените значение определенного ключа в словаре и выведите обновленный словарь на экран.

sex["Anna"] = 'male'
print(sex)

del sex['Anna']

sex['Dasha'] = 'no human'

# Проверьте, есть ли определенный ключ в словаре.

for i in sex.keys():
    if i == 'Dasha':
        print(f'{i} - Вы конченная мадама')
    else:
        print('Нормальный человек')

# Получите все ключи из словаря и выведите их на экран.

sex['Andrey'], sex['Anna'], sex['Marina'] = 'male', 'female', 'female'

del sex['Dasha']
for i in sex.keys():
    print(i)

# Получите все значения из словаря и выведите их на экран.

print('*' * 10)
for value in sex.values():
    print(value)

# Получите кортеж ключей, упорядоченных по возрастанию.

my_tuple = []
print('*' * 10)
for key in sex.keys():
    my_tuple.append(key)

my_tuple = tuple(my_tuple)
print(sorted(my_tuple))


# Получите кортеж значений, упорядоченных по возрастанию.

my_tuple_1 = []
for value in sex.values():
    my_tuple_1.append(value)

my_tuple_1 = tuple(my_tuple_1)
print(sorted(my_tuple_1))
