
day_one = int(input('Сколько километров спортсмен пробежал в первый день: '))
last_day = int(input('Каков желаемый результат: '))
count = 1
while day_one <= last_day:
    day_one *= 1.1
    count += 1
print(f'На {count} день спортсмен достиг результата')


input('\n\nНажмите Enter, чтобы выйти')
