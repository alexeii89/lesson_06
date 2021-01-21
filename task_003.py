class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._i = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.n} {self.s}')

    def get_total_income(self):
        pay = self._i.get("wage") + self._i.get("bonus")
        print(f'Доход с учетом премии: {pay}')

worker_1 = Position("Тест", "Тестов", "Менеджер", 30000, 5000)

worker_1.get_full_name()
worker_1.get_total_income()