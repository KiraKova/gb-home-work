class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Началась отрисовка {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'



pencil = Pencil('Карандаш')
pen = Pen('Ручка')
handle = Handle('Маркер')

print(pencil.draw())
print(handle.draw())
print(pen.draw())