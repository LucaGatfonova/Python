def my_func():
    arg_1 = float(input('Введите первое число: '))
    arg_2 = float(input('Введите второе число: '))
    arg_3 = float(input('Введите третье число: '))
    arr = [arg_1, arg_2, arg_3]
    arr.remove(min(arg_1, arg_2, arg_3))
    return round(sum(arr), 2)


print((f'Сумма двух наибольших аргументов равна:  {my_func()}'))
