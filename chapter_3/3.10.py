# Все функции: придумайте информацию, которую можно было бы хранить в списке. Например, создайте список гор, рек, стран, городов, языков... словом, чего угодно. Напишите программу, которая создает список элементов, а затем вызывает каждую функцию, упоминавшуюся в этой главе, хотя бы один раз.

compliments = ['cute', 'affectionate', 'caring', 'honest',
               'friendly', 'true', 'indispensable', 'strong', 'smart', 'sexy']

for compliment in compliments:
    print(f'Luda is {compliment.title()}')

print(sorted(compliments))
print(compliments[4])
print(compliments[-1])
compliments[4] = 'sexy1'
print(compliments[4])
compliments.append('charming')
compliments.insert(0, 'delightful')
del compliments[4]
pop_compliment = compliments.pop()
compliments.remove('true')
