# Домашние животные: создайте несколько словарей, имена которых представляют клички домашних животных. В каждом словаре сохраните информацию о виде животного и имени владельца. Сохраните словари в списке с именем pets. Переберите элементы списка. В процессе перебора выведите всю имеющуюся информацию о каждом животном.

pets = {
    'doggie': {
        'animal': 'dog',
        'owner': 'John'
    },
    'kitty': {
        'animal': 'cat',
        'owner': 'Mary'
    },
    'birdie': {
        'animal': 'bird',
        'owner': 'Sarah'
    },
    'hamster': {
        'animal': 'hamster',
        'owner': 'Bob'
    }
}

# for pet in pets:
#     for animal, owner in pet.items():
#         print(f'{animal} - {owner}')


for name_pet, params in pets.items():
    print(f'\n\tИмя питомца: {name_pet.title()}\n\tВид животного: {
          params['animal'].title()}\n\tИмя хозяина: {params['owner'].title()}')
