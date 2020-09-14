def div():
    try:
        а = float(input('Введите первое число (числитель): '))
        b = float(input('Введите второе число (знаменатель): '))
        result = round(а / b, 2)
    except ZeroDivisionError:
        return 'Ошибка!Деление на ноль!'
    return result
print((f'Результат:  {div()}'))
