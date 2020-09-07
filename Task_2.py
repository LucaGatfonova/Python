a = int(input('Введите число'))
hour = a // 3600
minute = a % 3600 // 60
second = a % 3600 % 60
print(f'{hour:02}:{minute:02}:{second:02}')
