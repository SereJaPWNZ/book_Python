# Топпинг для пиццы: напишите цикл, который предлагает пользователю вводить дополнения для пиццы до тех пор, пока не будет введено значение 'quit'. При вводе каждого дополнения выведите сообщение о том, что это дополнение включено в заказ.

flag = True
while flag:
    text = input('Введите топпинг для пиццы (или ‘quit’ для окончания): ')
    if text == 'quit':
        flag = False
