
sec = int(input('Введите время в секундах: '))
min = sec // 60
sec = sec % 60
hour = min // 60
min = min % 60
print(f'Ваше время в формате чч:мм:сс  {hour} : {min} : {sec}')


input('\n\nНажмите Enter, чтобы выйти')
