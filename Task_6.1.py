word = input("Введите слово >>> ")
def int_func(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]
print(int_func(word))

text = input("Введите слова через пробел >>> ").split()
res = []
for word in text:
    res.append(int_func(word))
print(' '.join(res))