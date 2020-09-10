month_dict = {'Зима': (1, 2, 12),
              'Весна': (3, 4, 5),
              'Лето': (6, 7, 8),
              'Осень': (9, 10, 11)}
month = int(input('Введите месяц в виде числа: '))
for key in month_dict.keys():
    if month in month_dict[key]:
        print(key)
