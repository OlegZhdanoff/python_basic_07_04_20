"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

words = []
name = []
proceeds = 0
costs = 0
company = dict()
avg_profit = 0

try:
    with open('example_7.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                if not word.isdigit():
                    name.append(word)
                elif not proceeds:
                    proceeds = int(word)
                else:
                    costs = int(word)
            company.update({' '.join(name[:(len(name)-1)]): proceeds - costs})
            name = []
            proceeds = 0

except Exception as e:
    print(e)

i = 0
for item in company.values():
    if item > 0:
        avg_profit += item
        i += 1
avg_profit /= i
company_profit = {'average_profit': avg_profit}
final_lst = [company, company_profit]

with open('example_7.json', 'wt', encoding='utf-8') as file:
    json.dump(final_lst, file, ensure_ascii=False)

