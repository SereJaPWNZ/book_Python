# Больше условий: количество условий не ограничивается десятью. Попробуйте написать другие условия и включить их в conditional_tests.py. Программа должна выдавать по крайней мере один истинный и один ложный результат для следующих видов проверок:
# • Проверка равенства и неравенства строк.
# • Проверки с использованием функции lower().
# • Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше или равно», «меньше или равно».
# • Проверки с ключевым словом and и or.
# • Проверка вхождения элемента в список.
# • Проверка отсутствия элемента в списке.

car_model = 'mazda'
print(car_model == 'mazda')
print(car_model != 'Mazda')
print(car_model.lower() == 'mazda')
my_number = 4
print(my_number == 4)
print(my_number != 5)
print(my_number > 4)
print(my_number < 5)
print(my_number <= 5)
print(my_number >= 5)
print(my_number > 3 and car_model == 'mazda')
print(my_number < 0 or car_model == 'mazda')
list_car = ['Toyota', 'Honda', 'Nissan', 'Mitsubishi',
            'Suzuki', 'Ford', 'Chevrolet', 'Mercedes-Benz', 'BMW']
if car_model.title() not in list_car:
    print(f'Марки автомобиля {car_model.title()} нет в нашем автосалоне')
car_model = 'Ford'
print(car_model.title() in list_car)
