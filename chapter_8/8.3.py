# Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст, который должен быть напечатан на ней. Функция должна выводить сообщение с размером и текстом.

def make_shirt(size, text_tshirt):
    print(f'Размер Вашей футболки: {
          size}\nТекст: который будет напечатан: "{text_tshirt.title()}"')


make_shirt(58, 'Топ футболка')
