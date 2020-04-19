"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""


from itertools import count, cycle

my_lst = [5, 6, 8, 3, 1, 99]
try:
    num = int(input('Введите число или что-нибудь другое'))
    for i in count(num):
        print(i)
except ValueError:
    for el in cycle(my_lst):
        print(el)
