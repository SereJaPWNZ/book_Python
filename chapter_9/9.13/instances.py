# - Смоделируйте 10 бросков каждого кубика.

'''Набор класса для вывода значения кубика'''
from class_die import Die

sided_cube_6 = Die()
sided_cube_10 = Die(10)
sided_cube_20 = Die(20)
list_cube_throw_6, list_cube_throw_10, list_cube_throw_20= [], [], []

for i in range(10):
    list_cube_throw_6.append(sided_cube_6.roll_die())
    list_cube_throw_10.append(sided_cube_10.roll_die())
    list_cube_throw_20.append(sided_cube_20.roll_die())
print(f'Значения результатов броска кубика с:\n- 6 сторонами: {list_cube_throw_6}\n- 10 сторонами: {list_cube_throw_10}\n- 20 сторонами:  {list_cube_throw_20}')
