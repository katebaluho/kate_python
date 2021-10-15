"""3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    max_el =  arg_list.pop(arg_list.index(max(arg_list)))
    max_el2 = arg_list.pop(arg_list.index(max(arg_list)))
    print (max_el + max_el2)

my_func(111, 22, 65)
my_func('aaa', 'qq', '65')
my_func(156.0, 64.23, 10.0)
