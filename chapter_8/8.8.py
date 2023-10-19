# Пользовательские альбомы: начните с программы из упражнения 8.7. Напишите цикл while, в котором пользователь вводит исполнителя и название альбома. Затем в цикле вызывается функция make_album() для введенных пользователей и выводится созданный словарь. Не забудьте предусмотреть признак завершения в цикле while.


text_exit = 'Если передумаете, будем снова рады Вас видеть в нашем приложении'


def make_album(name_executor, name_album, count_paths=None):
    full_composition = {'Executor': name_executor.title(),
                        'Album': name_album.title()}
    if count_paths:
        full_composition['count_paths'] = count_paths
    return full_composition


while True:
    print('Для выхода из программы введите символ "q" в любое из запрашиваемых полей')

    name_executor = input('\nВведите название музыкальной группы: ')
    if name_executor.lower() == 'q' or name_executor.lower() == 'й':
        print(text_exit)
        break
    name_album = input('\nВведите название альбома: ')
    if name_album.lower() == 'q' or name_album.lower() == 'й':
        print(text_exit)
        break
    count_paths = input('\nВведите количество дорожек: ')
    if count_paths.lower() == 'q' or count_paths.lower() == 'й':
        print(text_exit)
        break
    album = make_album(name_executor, name_album, count_paths)
    print(f'{"-"*100}\n{album}')
