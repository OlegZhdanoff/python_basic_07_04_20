"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv(
)).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
числа. """


class Cell:

    def __init__(self, num: int):
        self.qty = num

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        tmp = self.qty - other.qty
        if tmp > 0:
            return Cell(tmp)
        else:
            print('Клеток не может стать меньше нуля')
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(round(self.qty / other.qty))

    def make_order(self, num):
        tmp_str = ''
        for i in range(self.qty // num):
            tmp_str += '*' * num
            if i < (self.qty // num - 1):
                tmp_str += '\n'
        if self.qty % num:
            tmp_str += '\n' + ('*' * (self.qty % num))
        return tmp_str


c1 = Cell(8)
c2 = Cell(3)
c3 = c1 / c2
print(c1.make_order(3))
print(c3.qty)

