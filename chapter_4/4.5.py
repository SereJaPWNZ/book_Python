# Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь функциями min() и max() и убедитесь в том, что список действительно начинается с 1 и заканчивается 1 000 000. Вызовите функцию sum() и посмотрите, насколько быстро Python сможет просуммировать миллион чисел.

numbers = []
for i in range(1, 1_000_001):
    numbers.append(i)
sum_numbers = sum(numbers)
print(min(numbers), max(numbers), sum_numbers, sep='\n')
