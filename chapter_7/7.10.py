# Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск. Включите блок кода для вывода результатов опроса.

places_relax = []
flag = True
while flag:
    name_place = input('Введите место, которое хотите поситить: ')
    places_relax.append(name_place)
    choice = input('Вы хотите дописать еще места(Да(Yes)/Нет(No))? ')
    if choice.title() == 'Да' or choice.title() == 'Yes':
        continue
    else:
        flag = False
        print('Спасибо за Ваш ответ!')
