"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    speed = 0
    color = 'red'
    name = 'lada'
    is_police = False

    def __init__(self, clr='red', nam='lada'):
        self.color = clr
        self.name = nam

    def go(self, spd):
        self.speed = spd
        print(f'{self.name} - Go!')

    def stop(self):
        self.speed = 0
        print(f'{self.name} - Stop')

    def turn(self, direction):
        print(f'{self.name} turn to the {direction}')


class TownCar(Car):
    __max_passengers = 0
    __passengers = 0

    def __init__(self, max_pass, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__max_passengers = max_pass

    def go(self, spd):
        self.speed = spd
        if spd > 60:
            print("Your speed is too fast!")

    def add_passenger(self, num):
        if self.__max_passengers < (self.__passengers + num):
            self.__passengers += num
        else:
            print('Not enough space!')

    def remove_passengers(self, num):
        if (self.__passengers - num) >= 0:
            self.__passengers -= num
        else:
            print('Too many passengers to remove')


class SportCar(Car):

    def turbo(self, status=False):
        if status:
            self.speed *= 2
        else:
            self.speed //= 2


class WorkCar(Car):
    max_tonnage = 0
    tonnage = 0

    def __init__(self, weight, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_tonnage = weight

    def go(self, spd):
        self.speed = spd
        if spd > 40:
            print("Your speed is too fast!")

    def load(self, weight):
        if (self.tonnage + weight) > self.max_tonnage:
            self.tonnage += weight
        else:
            print("It's too heavy...")

    def unload(self, weight):
        if (self.tonnage - weight) >= 0:
            self.tonnage -= weight
        else:
            print("I don't have this weight")


class PoliceCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


baklazhan = Car('green', 'lada sedan')
bus = TownCar(12, 'yellow', 'gazel')
coupe = SportCar('red', 'dodge challenger')
truck = WorkCar(20, 'white', 'MAN')
police_car = PoliceCar('blue', 'ford')

baklazhan.go(100)
baklazhan.stop()

bus.go(80)
bus.go(60)
bus.add_passenger(5)
bus.add_passenger(20)
bus.stop()

coupe.go(10)
coupe.turbo(True)
print('Speed on turbo', coupe.speed)
coupe.stop()

truck.go(100)
truck.load(10)
truck.load(30)
print(f'{truck.name} - your weight {truck.max_tonnage}')
truck.unload(10)

police_car.go(30)
print('Is this police? -', police_car.is_police)

