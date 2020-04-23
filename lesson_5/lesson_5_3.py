"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""


from statistics import mean

employees = dict()
try:
    with open('example_3.txt', 'rt', encoding='utf-8') as file:
        for el in file.readlines():
            tmp = el.split()
            if len(tmp) == 2:
                if tmp[1].isdigit():
                    employees.update({tmp[0]: int(tmp[1])})
                    if int(tmp[1]) < 20000:
                        print(f'{tmp[0]} имеет оклад менее 20000')
except Exception as e:
    print(e)
    exit()

print(f'Средняя величина дохода: {mean(employees.values()):0.2f}')
