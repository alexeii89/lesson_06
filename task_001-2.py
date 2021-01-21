from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]
#        {"red": ['31m', 7], "yellow": ["33m", 2], "green": ["32m", 8]}
        self.key = 0

    def running(self):
        if self.key == 3:
            self.key =0
        print(self.__color[self.key])
        self.key += 1
        if self.__color[self.key] == 0:
            time = 7
        elif self.key == 1:
            time = 2
        else:
            time = 8
        sleep(time)


light = TrafficLight()
light.running()
light.running()
light.running()
light.running()
# не совсем понял задание но можно сделать
