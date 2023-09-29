# Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов. Придумайте пять простых блюд и сохраните их в кортеже.
# • Используйте цикл for для вывода всех блюд, предлагаемых рестораном.
# • Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается вносить изменения.
# • Ресторан изменяет меню, заменяя два элемента другими блюдами. Добавьте блок кода, который заменяет кортеж, и используйте цикл for для вывода каждого элемента обновленного меню.

dishes = ("Pancakes", "Omelette", "Spaghetti",
          "Fried Chicken", "Grilled Salmon")
print('Old tuple:')
print()
for dish in dishes:
    print(dish)

# dishes[0] = 'Steak'

dishes = dishes = ("Steak", "Pizza", "Burger", "Fries", "Salad")
print()
print('New tuple:')
for dish in dishes:
    print(dish)