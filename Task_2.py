with open('test.txt', 'r', encoding="utf-8") as content:
    content = content.readlines()
    print(f'Количество строк в файле: {len(content)}')
for line in content:
    word = line.split()
    count_word = len(word)
    print(f'Количество слов в строках:{count_word}')
