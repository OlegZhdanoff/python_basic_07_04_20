"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def user_info(name, surname, birthday, city, email, phone):
    print(f'Имя - {name}, Фамилия - {surname}, Год рождения - {birthday}, Город проживания - {city}, '
          f'email - {email}, Телефон - {phone}')


user_info(name='Ivan', city='Moscow', surname='Ivanov', phone='123', birthday='2000', email='qq@qq.qq')
