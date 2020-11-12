
earn = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек фирмы: '))

if earn > cost:
    print('Фирма работает в прибыль')
    rent = (earn - cost) / earn
    print(f'С рентабельностью {rent}')
    personal = int(input('Введите количество сотрудников фирмы: '))
    profit_on_one = (earn - cost) / personal
    print(f'Прибыль в расчете на одного сотрудника равняется {profit_on_one}')
elif earn == cost:
    print('Фирма работает в 0')
else:
    print('Фирма работает в убыток')


input('\n\nНажмите Enter, чтобы выйти')
