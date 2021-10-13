# Дано 2 целых числа, написать алгоритм поиска наибольшего общего делителя

number1 = 48
number2 = 0

while number1 != 0 and number2 != 0:
    if(number1 > number2):
        number1 = number1 % number2
    else:
        number2 = number2 % number1

print('НОД:', number1+number2)