rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open('text_4.txt', 'r', encoding="utf-8") as eng_file:
    for i in eng_file:
        i = i.split(' ', 1)
        rus_file.append(rus[i[0]] + i[1])
    print(rus_file)

with open('file_4_new.txt', 'w', encoding="utf-8") as rus_file_1:
    rus_file_1.writelines(rus_file)
