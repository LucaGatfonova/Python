from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(f'\033[31m {TrafficLight.__color[i]}')
                sleep(7)
            elif i == 1:
                print(f'\033[33m {TrafficLight.__color[i]}')
                sleep(2)
            elif i == 2:
                print(f'\033[32m {TrafficLight.__color[i]}')
                sleep(7)
            i += 1


TrafficLight().running()
