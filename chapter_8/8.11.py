# Архивированные сообщения: начните с программы из упражнения 8.10. Вызовите функцию send_messages() для копии списка сообщений. После вызова функции выведите оба списка и убедитесь в том, что в исходном списке остались все сообщения.


def sent_messages(messages, complited_sents):
    '''Отправка сообщения и добавление его в список sent_messages'''
    while messages:
        sent_message = messages.pop()
        complited_sents.append(sent_message)
        print('\nСообщение отправлено')


def show_messages(complited_sents):
    '''Показ пользователю доставленного сообщения'''
    for complited_sent in complited_sents:
        print(complited_sent)


messages = ['Привет!', 'Как дела?', 'Что нового?',
            'Рад тебя видеть', 'Хорошего дня!']
complited_sents = []

sent_messages(messages[:], complited_sents)
show_messages(complited_sents)

print(messages, complited_sents, sep='\n')
