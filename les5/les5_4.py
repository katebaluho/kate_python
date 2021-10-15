"""4
Функция принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без операторов ** * (без умножения и без возведения в степень).
Можно и нужно использовать сложение (+) и возможно деление (/)
"""


def in_power(number, x):
    return sum([number for i in range(x)])


def my_func(x, y):
    number_in_power = x
    counter = 1
    while counter < y:
        number_in_power = in_power(number_in_power, x)
        counter += 1
    return number_in_power


print('number_in_power', my_func(3, 5))
print('test number', 3 ** 5)
