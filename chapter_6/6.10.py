# 6.10. Любимые числа: измените программу из упражнения 6.2 (с. 114), чтобы для каждого человека можно было хранить более одного любимого числа. Выведите имя каждого человека в списке и его любимые числа.

peopls = {'Andrey': [1, 2], 'Kolia': [1, 2],
          'Ivan': [1, 2], 'Vlad': [1, 2], 'Jack': [1, 2]}
for people in peopls:
    print(f'У {people} любимые число - {peopls[people]}')
