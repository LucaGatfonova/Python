class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print (f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print ('Доход с учетом премии:')
        print(self._income.get('wage') + self._income.get('bonus'))

a = Position('Василий', 'Кислицын', 'Инженер', 100000, 25000)
a.get_full_name()
print(f'Должность: {a.position}')
a.get_total_income()
