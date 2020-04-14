def input_int(msg):
    str = input(f'{msg}\n')
    while True:
        if not str.isdigit():
            str = input('Ошибка! Введите целое положительное число\n')
            continue
        else:
            return int(str)


revenue = input_int('Введите выручку фирмы')
costs = input_int('Введите издержки фирмы')
profit = revenue - costs

if profit > 0:
    print(f'Ваша компания работает в прибыль\nРентабельность выручки равна {profit / revenue:0.2f}')
    employees_qty = input_int('Введите количество сотрудников в Вашей компании')
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {profit / employees_qty:0.2f}')
else:
    print('Ваша компания работает в убыток...')
