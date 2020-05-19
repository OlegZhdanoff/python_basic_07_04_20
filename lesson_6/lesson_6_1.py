"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
import time


class TrafficLight:
    __color = ''
    __modes = (('red', 7),
               ('yellow', 2),
               ('green', 4),
               )

    def running(self, clr):
        for i, mode in enumerate(self.__modes):
            if (clr == mode[0] and self.__color == self.__modes[i - 1][0]) or not self.__color:
                self.__color = clr
                print(self.__color)
                time.sleep(mode[1])
                return 0
        return print('Wrong light!')


traffic_light = TrafficLight()

traffic_light.running('red')
traffic_light.running('yellow')
traffic_light.running('green')
traffic_light.running('yellow')
