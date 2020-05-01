"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


try:
    with open('test.txt', 'wt', encoding='UTF-8') as file:
        while True:
            usr_data = input('Введите данные либо нажмите Enter\n')
            if not usr_data:
                break
            file.write(f'{usr_data}\n')
except Exception as e:
    print(e)
