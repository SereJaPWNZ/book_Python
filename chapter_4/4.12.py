# 12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла for для вывода каждого списка.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('calzone')

for foods in my_foods:
    print(foods, sep='')
print()
for foods in friend_foods:
    print(foods, sep='')
