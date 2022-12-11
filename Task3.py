"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func():
    arg1 = int(input("enter first argument ")),
    arg2 = int(input("enter second argument ")),
    arg3 = int(input("enter third argument ")),
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg2 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

my_sum = my_func()
print(f'Result - {sum(my_sum)}')
