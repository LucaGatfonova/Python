month = int(input('Введите месяц в виде числа: '))
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month == month_list[0] or month == month_list[1] or month == month_list[2]:
    print("Зима")
elif month == month_list[3] or month == month_list[4] or month == month_list[5]:
    print("Весна")
elif month == month_list[6] or month == month_list[7] or month == month_list[8]:
    print("Лето")
elif month == month_list[9] or month == month_list[10] or month == month_list[11]:
    print("Осень")
else:
    print('Ошибка, в году только 12 месяцев')
