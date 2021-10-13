# Write a function that adds from two invocations.
# add(3)(4)  // 7
# add(12)(20) // 32  Замыкание

# def add(a):
#     def helper(b):
#         return a+b
#     return helper

# add=lambda a:lambda b:a+b
#
# print(add(5)(12))
# print(add(20)(12))

# You notice there are different tree sizes but
# there's always one size which is unbalanced. ' \
#     'For example there are 2 size 2, 2 size 1 and 1 size 3. (then the size 3 is unbalanced)

# def find_the_missing_tree(trees):
#     new_set = set(trees)
#     count_dict = { }
#     for number in new_set:
#         count_dict.update({trees.count(number) : number})
#
#     return count_dict[min(count_dict.keys())]
#
# def find_the_missing_tree(trees):
#   return sorted(trees, key=trees.count)[0]

# Write a function that receives two strings as parameter.
# This strings are in the following format of date: YYYY/MM/DD.
# Your job is: Take the years and calculate the difference between them.
#
# def how_many_years (date1,date2):
#     print(int(date1[:4]))
#     return abs(int((date2.split('/'))[0])-int((date1.split('/'))[0]))
#
# print(how_many_years('2012/10/10', '2010/10/10'))

#utils.py

# numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
# even = []
# odd = []
# append_dict = {True: even.append, False: odd.append}
#
# def distribute_value(value):
#     append_dict[value % 2 == 0](value)
#
# list(map(distribute_value, numbers))
# print(even)
# print(odd)

dict_1 =  {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    }
dict_2= {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
users = (dict_1, dict_2)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

print(templates[dict_2["age"] < 7].format(name = dict_2["name"], surname = dict_2["surname"]))



# Нужно найти след матрицы(сумму элементов главной диагонали), 
# при этом размер матрицы вводит пользователь,и саму матрицу заполнять случайными числами.

# import random  
 
# def creatArray():
#     print('Введите первый индекс матрицы: ')
#     x = int(input())
#     print('Введите второй индекс матрицы: ')
#     y = int(input())
#     return [[random.randint(0,100) for i in range(x)] for j in range(y)]
 
# def sunction(array):
#     return sum([array[i][i] for i,_ in enumerate(array) if i < len(array[0])])

# print("Сумма элементов ",sunction(creatArray()))