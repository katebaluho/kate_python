"""
sum - 
- Входные данные: iter_obj = некий итерируемый объект на вход start по дефолту равен 0
старт используется как опопрный объект для сложения первого элемента
- Что она делает: суммирует все элементы итерируемого объекта поданного на вход
- Выходные данные - Сумма элементов
"""
from les4 import some_list


"""
Нейминг функций:
1 Понятное имя
2 стилистика такаяже как у переменных
3 Функции не Именуются как константы
"""
import datetime


def my_sum(iter_obj, start=0):
    """
    Функция сумматор, складывает объекты итерируемого объекта опираясь на переменную start
    """
    for itm in iter_obj:
        start += itm
    return start


"""
enumerate 
- входные данные итерируемый объект start число начала итерации
- что делает формирует кортеж где 0 индекс это номер счетчика и 1 индекс это элемент итерируемого объекта
- возвращается кортеж кортежей
"""


def my_enumerate(iter_obj, start=0):
    result = zip(range(start, start + len(iter_obj)), iter_obj)
    return tuple(result)


def some(func, data):
    call_str = f"{datetime.datetime.now()} CAllED FUNCTION {func.__name__}"
    print(call_str)
    result = func(data)
    print("END")
    return result


hello = [1, 2, 3, 4, 5, 6]

# def example_func():
#     # hello = [4, 5, 6]
#     def wrap():
#         return sum(hello)
#     return wrap
# result = example_func()
# print(result())

# a = 1
# b = 2
# 
# def example_func2():
#     # hello = [0, 1, 2]
#     global hello
#     global a
#     hello = [0, 10, 22]
#     a = 22
#     b = 15
#     return sum(hello)
# 
# 
# print(example_func2())
# print(a, b)


a = 2
b = 5

# if a > b:
#     c = a
# else:
#     c = 15
# 
# c = 15
# if a > b:
#     c = a

c = a if a > b else 15


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def some_none(a, b):
    if a is None:
        return b ** 1
    if b is None:
        return a ** 1


some_list = [2, 3, 4, 5, 6, 7, 8, 9]
# 2, 3
# [None, 4, 5, 6, 7, 8, 9]
# # None, 4 
# [4, 5, 6, 7, 8, 9]

import functools


def my_reduce(func, iter_obj):
    flag = True
    result = None
    for itm in iter_obj:
        if flag:
            result = itm
            flag = not flag
            continue
        result = func(result, itm)
    return result


# result = 2 / 3/ 4/ 5/ 6/ 7/ 8/ 9

# start = 1
# for itm in some_list:
#     start = mul(start, itm)
# print(start)
# 
# print(my_reduce(div, some_list))
# print(functools.reduce(div, some_list))

# map - Принимает на вход функцию и итеририруемый объект и возвращается итератор
some_list_2 = [9, 8, 7, 6, 5, 5]


# result = []
# for itm in zip(some_list, some_list_2):
#     result.append(sum(itm))

def my_map(func, iter_obj):
    result = []
    for itm in iter_obj:
        result.append(func(itm))


# 
# result = list(map(sum, zip(some_list, some_list_2)))
# print(result)
def some_func(n):
    return n ** 2 if n & 1 else n ** 3


result = list(map(lambda n: n ** 2 if n & 1 else n ** 3, some_list_2))
print(result)

anon_func = (lambda x: x**2)(3)