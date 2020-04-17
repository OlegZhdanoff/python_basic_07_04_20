"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""


def my_func(a, b, c):
    minimum = a
    if minimum > b:
        minimum = b
    if minimum > c:
        minimum = c
    return a + b + c - minimum


print(my_func(6, 4, 5))
