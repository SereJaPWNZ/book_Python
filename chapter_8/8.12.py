# Сэндвичи: напишите функцию, которая получает список компонентов сэндвича.
# Функция должна иметь один параметр для любого количества значений, переданных при вызове функции, и выводить описание заказанного сэндвича. Вызовите функцию три раза с разным количеством аргументов.


def conclusion_components(*components_sandwich):
    '''Вывод компонетов сэндвича'''
    print('\nИз чего состоит сэндвич:')
    for component_sandwich in components_sandwich:
        print(f'- {component_sandwich}')


conclusion_components('булка', 'сыр', 'огурцы', 'котлета', 'соус')
conclusion_components('сыр', 'огурцы')
conclusion_components('котлета', 'соус')
