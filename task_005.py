class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        if self.title == "Stationery":
            print("Запуск отрисовки.")
        else:
            print(f'Рисуем {self.title}')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
