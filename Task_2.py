from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def fabric_consumption(self):
        return round(self.height * 2 + 0.3)


size = 44
height = 160
coat = Coat(size)
print(f'Расход ткани на пошив пальто: {coat.fabric_consumption()}')

suit = Suit(height)
print(f'Расход ткани на пошив костюма: {suit.fabric_consumption()}')
print(f'Общий расход ткани: {suit.fabric_consumption() + coat.fabric_consumption()}')
