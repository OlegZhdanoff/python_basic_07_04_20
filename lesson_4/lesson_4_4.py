"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""


number_lst = [3, 3, 5, 1, 4, 5, 8, 9, 1]
tmp_lst = [*reversed(number_lst)]

result_lst = [*reversed([el for i, el in enumerate(tmp_lst) if tmp_lst[i+1:].count(el) == 0])]

"""
Более читабельная версия как мне кажется, но при этом генератор используется практически только номинально
for el in tmp_lst:
    if tmp_lst.count(el) > 1:
        tmp_lst.remove(el)
result_lst = [el for el in reversed(tmp_lst)]
"""


print(f"Начальный список\n{number_lst}")
print(f'Результат\n{result_lst}')
