words = input('Введите слова через пробел')
for ind, i in enumerate(words.split(), 1):
    print(ind, i[:10])
