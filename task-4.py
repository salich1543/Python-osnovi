
n = int(input('Введите число: '))
max = n % 10

while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10

print(max)

input('\n\nНажмите Enter, чтобы выйти')
