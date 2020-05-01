"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, nam):
        self.name = nam

    @abstractmethod
    def consumption(self) -> float:
        pass


class Suit(Clothes):

    def __init__(self, height, *args, **kwargs):
        self.height = height
        super().__init__(*args, **kwargs)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def consumption(self) -> float:
        return self.height * 2 + 0.3


class Coat(Clothes):

    def __init__(self, siz, *args, **kwargs):
        self.size = siz
        super().__init__(*args, **kwargs)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, num):
        self.__size = num

    def consumption(self) -> float:
        return self.size / 6.5 + 0.5


coat = Coat(50, 'пальто')
suit = Suit(180, 'костюм')
print(f'Количество ткани на пошив "{coat.name}" - {coat.consumption():0.2f}')
print(f'Количество ткани на пошив "{suit.name}" - {suit.consumption():0.2f}')
