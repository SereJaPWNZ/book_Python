# Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет.

number = int(input('Введите число: '))
if number % 10 == 0:
    print('Число кратно 10')
else:
    print('Число не кратно 10')