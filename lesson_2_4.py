"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

i = 1
words = input('Введите строку')

for el in words.split(' '):
    print(i, el[:10])
    i += 1
