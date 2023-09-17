# Моя пицца, твоя пицца: начните с программы из упражнения 4.1. Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее:
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. Выведите сообщение «My favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение «My friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что каждая новая пицца находится в соответствующем списке.

pizzas = ['Napoletana', 'Calzone', 'Romana']
friend_pizzas = pizzas[:]
pizzas.append('Mushroom Pizza')
friend_pizzas.append('Sausage Pizza')
print(pizzas)
print(friend_pizzas)
