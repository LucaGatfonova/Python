x = abs(int(input('Введите x: ')))
y = abs(int(input('Введите y: ')))


def my_func(x, y):
    i = 1
    while y > 0:
        i *= x
        y = y - 1
    return 1 / i


print((f'Результат:  {my_func(x, y)}'))
