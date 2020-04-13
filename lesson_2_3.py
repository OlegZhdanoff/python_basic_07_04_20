"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

def input_int(msg):
    str = input(f'{msg}\n')
    while True:
        if not str.isdigit():
            str = input('Ошибка! Введите целое положительное число\n')
            continue
        else:
            return int(str)


month = input_int('Введите номер месяца')
while month < 1 and month > 12:
    print("Такого месяца не существует!")
    month = input_int('Введите номер месяца')

seasons = {"Зима": (1, 2, 12), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
for el in seasons:
    if month in seasons.get(el):
        print("Время года -", el)

