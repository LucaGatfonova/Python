my_f = open('test.txt', 'w', encoding="utf-8")
line = input('Введите текст \n')
while line:
    my_f.writelines(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()

