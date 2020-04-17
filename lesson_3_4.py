"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


is_not_end = 1
res = 0
while is_not_end:
    numbers_str = input('Введите строку чисел, разделенных пробелом, для выхода введите q\n')
    numbers_lst = numbers_str.split(' ')
    for el in numbers_lst:
        q_pos = el.find('q')
        if q_pos != -1:
            el = el[:q_pos]
            is_not_end = 0
        try:
            el = float(el)
        except ValueError:
            if is_not_end:
                print('Вы ввели не число, а что то другое...', el)
                continue
            else:
                print('Сумма чисел в строке равна', res)
                break
        res += el
    print('Сумма чисел в строке равна', res)
