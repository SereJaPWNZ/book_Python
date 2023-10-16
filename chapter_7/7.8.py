# Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле переберите элементы первого списка и выведите сообщение для каждого элемента (например, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка перемещается в список finished_sandwiches. После того как все элементы первого списка будут обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.

sandwich_orders = ['Крабовый сэндвич', 'Сэндвич с курицей и авокадо', 'Сэндвич с тунцом и майонезом', 'Сэндвич со сливочным сыром и ветчиной', 'Сэндвич с индейкой и овощами',
                   'Сэндвич с ростбифом и горчицей', 'Сэндвич с сыром и перцем', 'Сэндвич с беконом и томатами', 'Сэндвич с жареным яйцом и салатом', 'Сэндвич с фруктами и йогуртом']
finished_sandwiches = []
list_finished_sandwich = ''

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'I made your {finished_sandwich}')
    finished_sandwiches.append(finished_sandwich)
print('\nСписок всех изготовленных сендвичей: ')
for finished_sandwich in finished_sandwiches:
    list_finished_sandwich = ''.join(finished_sandwich.lower())
    print(list_finished_sandwich, end=', ')
