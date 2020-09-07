number = int(input('Введите число'))
b = number % 10
number = number // 10
if number > 0:
   while number > 0:
        if number % 10 > b:
            b = number % 10
        number = number // 10
   print(b)
else:
   print('Введите положительное число')
