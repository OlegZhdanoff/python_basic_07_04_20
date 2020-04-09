def input_int(msg):
    str = input(f'{msg}\n')
    while True:
        if not str.isdigit():
            str = input('Ошибка! Введите целое положительное число\n')
            continue
        else:
            return int(str)


a = input_int('Сколько километров пробежал спортсмен в первый день?')
b = input_int('Сколько километров хочет пробегать спортсмен?')
day = 1

while a < b:
    print(f'{day}-й день: {a:0.2f} км.')
    a *= 1.1
    day += 1

print(f'{day}-й день: {a:0.2f} км.')
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км.')
