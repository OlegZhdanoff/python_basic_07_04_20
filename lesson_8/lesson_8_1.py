"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """

import re


class Data:

    def __init__(self, dt: str):
        if self.isdata(dt):
            self.data = dt
        else:
            print('Invalid data format - ', dt)
            self.data = ''

    @classmethod
    def __int_extract(cls, dt: str) -> list:
        return list(map(int, (re.findall(r'\d+', dt))))

    @staticmethod
    def isdata(dt: str) -> bool:
        # простая проверка на дату, год ограничил до 2050
        if re.fullmatch(r'[0-3]{,1}\d[-][0-1]{,1}\d[-]\d{2,4}', dt):
            numbers_lst = Data.__int_extract(dt)
            if (0 < numbers_lst[0] < 32) and (0 < numbers_lst[1] < 13) and (0 < numbers_lst[2] < 2050):
                if numbers_lst[1] == 2:
                    # проверка года на високосность
                    if numbers_lst[2] % 4 == 0:
                        return True if numbers_lst[0] < 30 else False
                    else:
                        return True if numbers_lst[0] < 29 else False
                return True
        return False


test = Data('29-2-2020')
print(test.data)
