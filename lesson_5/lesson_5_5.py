"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

try:
    with open('example_5.txt', 'wt', encoding='utf-8') as file:
        for num in range(10):
            file.write(f'{randint(1, 10)} ')
except Exception as e:
    print(e)

try:
    with open('example_5.txt', 'rt', encoding='utf-8') as file:
        my_sum = sum(map(int, file.readline().split()))
except Exception as e:
    print(e)

print('Сумма чисел =', my_sum)
