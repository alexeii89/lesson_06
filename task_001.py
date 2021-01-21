from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = {"red": ['31m', 7], "yellow": ["33m", 2], "green": ["32m", 8]}
        self.etalon = ["red", "yellow", "green"]
        self.i = 0

    def running(self):
        for key in self.__color:
            if key != self.etalon[self.i]:
                print("Error!")
            else:
                print("\033[" + self.__color[key][0] + " {}".format(key))
                self.i += 1
                if self.i ==3:
                    self.i=0
            sleep(self.__color[key][1])




light = TrafficLight()
light.running()
# не понял зачем проверка.


