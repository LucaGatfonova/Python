def sum_func():
    number_sum = 0
    while True:
        number = input('Введите числа через пробел. Для выхода из программы, нажмите #: ').split()
        for i in range(len(number)):
            if number[i] != "#":
                number_sum = number_sum + int(number[i])
            else:
                break
        final_sum = 0
        final_sum = final_sum + number_sum
        print(final_sum)
        if "#" in number:
            print("Выполнение программы завершено!")
            break


sum_func()
