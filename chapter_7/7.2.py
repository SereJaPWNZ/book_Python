# Заказ стола: напишите программу, которая спрашивает у пользователя, на сколько мест он хочет забронировать стол в ресторане. Если введенное число больше 8, выведите сообщение о том, что пользователю придется подождать. В противном случае сообщите, что стол готов.

count_seats = int(input('How many places do you need to book: '))

if count_seats > 8:
    print('The user will have to wait')
else:
    print('Your table is ready!')
