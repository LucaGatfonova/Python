import random

arr = [random.randint(0, 10) for i in range(20)]

arr_2 = [i for i in arr if arr.count(i) < 2]

print(f'Исходный список: {arr}')
print(f'Результат: {arr_2}')
