"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
my_list = [5, 'строка', 7.34, complex(3, 4), ['qwe', 'rty'],(11, 22), {33,44}, True,]

for el in my_list:
    print(el, type(el))
