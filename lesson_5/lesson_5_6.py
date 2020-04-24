"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


try:
    with open('example_6.txt', 'rt', encoding='utf-8') as file:
        data = file.readlines()
except Exception as e:
    print(e)

lessons_dict = dict()
name = ''
is_name = False
digit = ''
digit_lst = []

for el in data:
    for letter in el:
        if (ord(letter.lower()) in range(97, 123) or ord(letter.lower()) in range(1072, 1103)) and not is_name:
            name += letter
        else:
            if len(name):
                is_name = True
            if letter.isdigit():
                digit += letter
            elif len(digit):
                digit_lst.append(int(digit))
                digit = ''

    lessons_dict.update({name: sum(digit_lst)})
    name = ''
    digit_lst = []
    is_name = False

print(lessons_dict)


# решение задачи с помощью регулярных выражений
import re
lessons_dict = dict()
for el in data:
    name = re.match(r'\s{0,}(\w+|\s+)*', el).group(0)
    digit_lst = re.findall(r'\d+', el)
    lessons_dict.update({re.sub(r'^\s*', '', name): sum(map(int, digit_lst))})
print(lessons_dict)
