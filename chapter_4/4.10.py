# Сегменты: добавьте в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее:
# • Выводит сообщение «The irst three items in the list are:», а затем использует сегмент для вывода первых трех элементов из списка.
# • Выводит сообщение «Three items from the middle of the list are:», а затем использует сегмент для вывода первых трех элементов из середины списка.
# • Выводит сообщение «The last three items in the list are:», а затем использует сегмент для вывода последних трех элементов из списка.

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f'The irst three items in the list are: {my_foods[:3]}')
print(f'Three items from the middle of the list are: {my_foods[1:4]}')
print(f'The last three items in the list are: {my_foods[-3:]}')
