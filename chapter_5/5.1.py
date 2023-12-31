# Проверка условий: напишите последовательность условий. Выведите описание каждой проверки и ваш прогноз относительно ее результата. Код должен выглядеть примерно так:
#    car = 'subaru'
#    print("Is car == 'subaru'? I predict True.")
#    print(car == 'subaru')
#    print("\nIs car == 'audi'? I predict False.")
#    print(car == 'audi')
# • Внимательно просмотрите результаты. Убедитесь в том, что вы понимаете, почему результат каждой строки равен True или False.
# • Создайте как минимум 10 условий. Не менее пяти одних должны давать результат True, а не менее пяти других — результат False.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print(car != 'Subaru')
print(car.title() == 'Subaru')
print(car != 'mazda')
print(car == car)
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print(car != 'subaru')
print(car != car)
print(car.lower() == 'Subaru')
