# Сокращение списка гостей: только что выяснилось, что новый обеденный стол привезти вовремя не успеют и места хватит только для двух гостей.
# • Сотавьте список из 7 гостей. Добавьте команду для вывода сообщения о том, что на обед приглашаются всего два гостя.
# • Используйте метод pop() для последовательного удаления гостей из списка до тех пор, пока в списке не останутся только два человека. Каждый раз, когда из списка удаляется очередное имя, выведите для этого человека сообщение о том, что вы сожалеете об отмене приглашения.
# • Выведите сообщение для каждого из двух человек, остающихся в списке. Сообщение должно подтверждать, что более раннее приглашение остается в силе.
# • Используйте команду del для удаления двух последних имен, чтобы список остался пустым. Выведите список, чтобы убедиться в том, что в конце работы программы список действительно не содержит ни одного элемента.

# 0
guests = ['ivan', 'andrey', 'vlad', 'timur', 'yardrey']
# 1
print('Дорогие друзья, в виду проблем с местами мы вынуждены сократить список гостей, приносим наши искренние извенения')
# 2
while len(guests) > 2:
    removed_guest = guests.pop(-1)
    print(f'Простите, {removed_guest.title()
                       }, но мы вынуждены отменить приглашение.')
# 3
print(f'Ваше приглашение, {guests[0]}, остается в силе\nВаше приглашение, {
      guests[1]}, остается в силе')

# 5
del guests[0], guests[0]
print(guests)
