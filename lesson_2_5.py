"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


def input_int(msg):
    str = input(f'{msg}\n')
    while True:
        if not str.isdigit():
            str = input('Ошибка! Введите целое положительное число\n')
            continue
        else:
            return int(str)


rating = [7, 5, 3, 3, 2]
rating_el = input_int('Введите рейтинг')

if rating_el in rating:
    rating.insert(rating.index(rating_el), rating_el)
else:
    for el in reversed(rating):
        if rating_el < el:
            rating.insert(rating.index(el)+1, rating_el)
            break
        elif rating.index(el) == 0:
            rating.insert(0, rating_el)

print(rating)
