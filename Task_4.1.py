x = abs(int(input('Введите x: ')))
y = -abs(int(input('Введите y: ')))


def my_func(x, y):
    return x ** y


print((f'Результат:  {my_func(x, y)}'))
