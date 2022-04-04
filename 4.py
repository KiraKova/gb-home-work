class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name}, {self.color} цвета поехала!'

    def stop(self):
        return f'Машина {self.name}, {self.color} цвета остановилась!'

    def turn_left(self):
        return f'Машина {self.name}, {self.color} цвета повернула налево'

    def turn_right(self):
        return f'Машина {self.name}, {self.color} цвета повернула направо'

    def show_speed(self):
        return f'Машина {self.name} цвета едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость транспорта {self.name}: {self.speed}')

        if self.speed > 40:
            return f'Привышение скорости транспортом {self.name}'
        else:
            return f'Транспорт {self.name} едет с нормальной скоростью'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость транспорта {self.name}: {self.speed}')

        if self.speed > 60:
            return f'Привышение скорости транспортом {self.name}'
        else:
            return f'Транспорт {self.name} едет с нормальной скоростью'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"Эта машина {self.name} полицейская"
        else:
            return f"Эта машина {self.name} не полицейская"


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(lada.turn_left())
print(f'When {oka.turn_right()}, then {audi.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {lada.name}  a police car? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.show_speed())
