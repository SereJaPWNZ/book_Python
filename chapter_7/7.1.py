# Прокат машин: напишите программу, которая спрашивает у пользователя, какую машину он бы хотел взять напрокат. Выведите сообщение с введенными данными (например, «Let me see if I can find you a Subaru”).

rental_car = input('Enter the brand of the car you want to rent: ')
print(f'Let me see if I can find you a {rental_car.title()}')
