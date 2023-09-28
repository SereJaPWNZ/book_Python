# Любимый фрукт: составьте список своих любимых фруктов. Напишите серию независимых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
# • Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
# • Напишите пять команд if. Каждая команда должна проверять, входит ли определенный тип фрукта в список. Если фрукт входит в список, блок if должен выводить сообщение вида «You really like bananas!».

favorite_fruits = ['Banana', 'Orange', 'Apple']
for fruit in favorite_fruits:
    if fruit == 'Banana':
        print('You really like bananas!')
    elif fruit == 'Orange':
        print('You really like oranges!')
    elif fruit == 'Apple':
        print('You really like apples!')
    else:
        print("You don't like " + fruit + ", do you?")
