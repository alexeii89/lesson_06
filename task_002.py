class Road:

    def __init__(self, _width, _length):
        self.weight = 25
        self.thickness = 5
        self.w = _width
        self.l = _length

    def calc(self):
        rez = self.w * self.l * self.weight * self.thickness
        print(f"Масса асфальта равна: {rez} кг")


Road_1 = Road(5000, 20)
Road_1.calc()
