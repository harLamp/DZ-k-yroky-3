"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def personal_data(name, surname, year, city, email, phone):
    return print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, '
                 f'Город проживания: {city}, Email: {email}, Телефон: {phone}')

personal_data(
    name=input('Введите Имя '),
    surname=input('Введите Фамилию '),
    year=int(input('Введите Ваш год рождения ')),
    city=input('Введите город '),
    email=input('Введите email '),
    phone=input('Введите телефон '),
)
