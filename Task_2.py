import random

a = random.sample(range(1, 300), 13)

new_list = [j for i, j in zip(a, a[1:]) if j > i]
print(f'Исходный список {a}')
print(f'Новый список {new_list}')
