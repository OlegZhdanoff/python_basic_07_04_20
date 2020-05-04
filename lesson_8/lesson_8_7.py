"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """


class Complex:

    def __init__(self, rez, imz):
        self.rez = rez
        self.imz = imz

    def __add__(self, other):
        return Complex(self.rez + other.rez, self.imz + other.imz)

    def __mul__(self, other):
        rez = self.rez * other.rez - self.imz * other.imz
        imz = self.rez * other.imz + other.rez * self.imz
        return Complex(rez, imz)

    def __str__(self):
        if self.imz < 0:
            return str(round(self.rez, 2)) + str(round(self.imz, 2)) + '*i'
        elif self.imz > 0:
            str(round(self.rez, 2)) + '+' + str(round(self.imz, 2)) + '*i'
        return str(round(self.imz, 2)) + '*i' if self.rez == 0 else str(round(self.rez, 2))


if __name__ == '__main__':
    num1 = Complex(-1.5, 0)
    num2 = Complex(0, -4.2)
    print(num1)
    print(num2)
    print(num1 + num2)
    print(num1 * num2)
