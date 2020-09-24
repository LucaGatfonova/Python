class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * self.volume


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume



r = MassCount(20, 5000, 125)
print(f'Масса асфальта равна: {int(r.mass()/1000)} т')