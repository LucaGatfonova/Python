income = int(input('Введите выручку компании в руб.'))
expense = int(input('Введите издержки компании в руб.'))
profit = (income - expense) / expense
if income > expense:
    print(f'Ваша компания сработала в Прибыль.Рентабельность выручки составила: {profit} руб.')
    people = int(input('Введите количество сотрудников в компании'))
    profit_people = (income - expense) / people
    print(f'Прибыль на 1 сотрудника:{profit_people} руб.')
else:
    print('Ваша компания сработала в Убыток')
