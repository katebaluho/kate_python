"""5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ (например Q), выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_input_number(number):
    return sum(list(map(lambda i: int(i), number)))


def user_input():
    result = 0
    while True:
        number = input("Enter numbers: ").split()
        if not ("Q" in number):
            result += sum_input_number(number)
            print("Sum of numbers: ", result)
        else:
            number.pop()
            result += sum_input_number(number)
            print("Sum of numbers: ", result)
            break
    return result


print('Result', user_input())
