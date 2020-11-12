
n = int(input('Введите число: '))
max_ = n % 10

while n >= 1:
    n = n // 10
    if n % 10 > max_:
        max_ = n % 10

print(max_)

input('\n\nНажмите Enter, чтобы выйти')
