class Car:

    def __init__(self, color, name):
        self.s = 0
        self.c = color
        self.n = name
        self.is_police = False

    def show_speed(self):
        print(self.s)

    def go(self, speed):
        self.s = speed
        print("Go-go ", self.s)

    def stop(self):
        self.s = 0
        print("Stop ", self.s)

    def turn(self, direction):
        if self.s > 0:
            print(f"машина повернула на {direction}")
        else:
            print(f'машина не едет!')


class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            print("превышение скорости")
        else:
            print(self.s)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            print("превышение скорости")
        else:
            print(self.s)


class PoliceCar(Car):
    def __init__(self):
        super.__init__(self.n, self.c, self.s)
        self.is_police = True

car_1 = WorkCar("green", "Ford")

car_1.go(70)
car_1.show_speed()
car_1.turn("left")
car_1.stop()
