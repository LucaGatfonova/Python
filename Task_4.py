from abc import ABC, abstractmethod

class Storehouse:
    # Подразделения
    @staticmethod
    def warehouse(self):
        print(f'Прием на склад {self.name}')

    @staticmethod
    def shop(self):
        print(f'Перемещение в магазин {self.name}')

    @staticmethod
    def service(self):
        print(f'Перемещение в сервисный центр {self.name}')

class StoreMashines(Storehouse):

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, 1-для перемещения в магазин,2-для перемещения в сервисный центр, продолжение - Enter')
        q = input(f'---> ')
        if q.lower() == 'q':
            self.my_store_full.append(self.my_store)
            print(f'На складе: \n {self.my_store_full}')
        elif q.lower() == '1':
            print(f'Перемещение в магазин {self.name}, количество {self.quantity}')
        elif q.lower() == '2':
            print(f'Перемещение в сервисный центр {self.name}, количество {self.quantity}')
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'печатает со скоростью {self.numb} листов в минуту'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'сканирует со скоростью {self.numb} листов в минуту'


class Copier(StoreMashines):
    def to_copier(self):
        return f'копирует со скоростью  {self.numb} листов в минуту'


unit_1 = Printer('hp', 2000, 8, 10)
unit_2 = Scanner('Canon', 1200, 3, 10)
unit_3 = Copier('Xerox', 1500, 2, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())