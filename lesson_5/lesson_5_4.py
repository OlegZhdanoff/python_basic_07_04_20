"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

numbers = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре',
           }


try:
    with open('example_4.txt', 'rt', encoding='utf-8') as file:
        with open('example_4_output.txt', 'wt', encoding='utf-8') as file_out:
            for i, line in enumerate(file):
                tmp_str = (line.split())
                tmp_str[0] = numbers.get(tmp_str[0])
                file_out.write(f'{" ".join(tmp_str)}\n')
except Exception as e:
    print(e)
