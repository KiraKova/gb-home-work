class Road:

    def __init__(self, _length, _width, v, b):
        self._lenght = _length
        self._width = _width
        self.v = v
        self.b = b

    def mass(self):
        return (self._lenght * self._width * self.v * self.b) / 1000


r = Road(20, 5000, 25, 5)

print(f'Результат: {int(r.mass())} т.')

