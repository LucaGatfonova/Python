with open('text_3.txt', 'r', encoding="utf-8") as content:
    salary = []
    name = []
    my_list = content.read().split('\n')
    for i in my_list:
        i = i.split()
        salary.append(i[1])
        if float(i[1]) < 20000:
            name.append(i[0])

    print(
        f'Сотрудники, имеющие оклад меньше 20.000 {name}, средняя величина дохода сотрудников: {sum(map(float, salary)) / len(salary)}')
