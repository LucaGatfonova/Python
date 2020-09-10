a = [int(i) for i in input("Введите через пробел числа от 1 до 9: ").split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
