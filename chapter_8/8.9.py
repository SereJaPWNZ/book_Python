# Сообщения: создайте список с серией коротких сообщений. Передайте список функции show_messages(), которая выводит текст каждого сообщения в списке.

messages = [
    'Привет!',
    'Как дела?',
    'Что нового?',
    'Рад тебя видеть',
    'Хорошего дня!'
]


def show_messages(messages):
    for message in messages:
        print(message)


show_messages(messages)
