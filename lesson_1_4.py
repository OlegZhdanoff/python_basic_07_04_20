num_str = input('Введите целое положительное число\n')

while True:
    if not num_str.isdigit():
        num_str = input('Ошибка! Введите целое положительное число\n')
        continue
    else:
        break

num = int(num_str)
maximum = num % 10
num //= 10

while True:
    if maximum < num % 10:
        maximum = num % 10
    num //= 10
    if num == 0:
        break
print(f'Максимальная цифра в числе {num_str} = {maximum}')
