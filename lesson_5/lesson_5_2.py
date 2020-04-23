"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


try:
    with open('example_2.txt', 'rt', encoding='utf-8') as file:
        lines = file.readlines()
except Exception as e:
    print(e)
    exit()
print('Количество строк в файле', len(lines))
for i, el in enumerate(lines):
    print(f'Строка #{i+1} ---- содержит {len(el.split())} слов')
