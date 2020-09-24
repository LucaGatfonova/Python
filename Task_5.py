class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('\033[34m')
        print(f'Запуск отрисовки.У вас {self.title} синего цвета')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('\033[36m')
        print(f'Запуск отрисовки.У вас {self.title} бирюзового цвета')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('\033[33m')
        print(f'Запуск отрисовки.У вас {self.title} желтого цвета')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()