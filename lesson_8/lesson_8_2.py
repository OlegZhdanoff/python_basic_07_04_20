"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    a, b = list(map(float, (input('Please enter two digits\n')).split()))
    if not b:
        raise DivisionByZero('Cannot be divided by zero')
    print(f'{a / b:0.2f}')
except ValueError:
    print("It's not a digit...")
except DivisionByZero as e:
    print(e)
