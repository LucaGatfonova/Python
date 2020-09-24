class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернул(а) направо')

    def turn_left(self):
        print(f'{self.name} повернул(а) налево')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч')

    def police(self):
        if self.is_police == True:
            print(f'{self.name} полицейская машина!')
        else:
            print(f'{self.name} не полицейская машина!')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} в городе {self.speed} км/ч')

        if self.speed > 60:
            print(f'Скорость {self.name} превышена!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч')

        if self.speed > 40:
           print(f'Скорость {self.name} превышена!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(100, 'Красная', 'Audi', False)
lada = TownCar(30, 'Белая', 'Lada', True)
tractor = WorkCar(60, 'Серебристый', 'Трактор', False)
ford = PoliceCar(110, 'Синий', 'Ford', True)

audi.go()
lada.turn_left()
tractor.turn_right()
audi.stop()
lada.go()

print(f'{lada.name} {lada.color} цвета')
audi.show_speed()
tractor.show_speed()
ford.show_speed()
lada.show_speed()

audi.police()
lada.police()
ford.police()
tractor.police()
