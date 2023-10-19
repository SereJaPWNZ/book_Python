# Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома. Функция должна получать имя исполнителя и название альбома и возвращать словарь, содержащий эти два вида информации. Используйте функцию для создания трех словарей, представляющих разные альбомы. Выведите все возвращаемые значения, чтобы показать, что информация правильно сохраняется во всех трех словарях.
# Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме, имеющий значение по умолчанию None. Если в строку вызова включено значение количества дорожек, добавьте это значение в словарь альбома. Создайте как минимум один новый вызов функции с передачей количества дорожек в альбоме.

def make_album(name_executor, name_album, count_paths=None):
    full_composition = {'Executor': name_executor, 'Album': name_album}
    if count_paths:
        full_composition['count_paths'] = count_paths
    return full_composition


musician_1 = make_album('Alisa', 'Up', count_paths=12)
musician_2 = make_album('Alisa2', 'Up2')
musician_3 = make_album('Alisa3', 'Up3', count_paths=100)

print(musician_1, musician_2, musician_3)
