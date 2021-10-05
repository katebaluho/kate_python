"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""

numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

all_number = [numbers[0] % 2, numbers[1] % 2, numbers[2] % 2, numbers[3] % 2, numbers[4] % 2, numbers[5] % 2,
              numbers[6] % 2, numbers[7] % 2, numbers[8] % 2, numbers[9] % 2, numbers[10] % 2]

print(all_number)  #[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]

even.append(numbers[3])
even.append(numbers[4])
even.append(numbers[8])
even.append(numbers[10])
print(even)

odd.append(numbers[0])
odd.append(numbers[1])
odd.append(numbers[2])
odd.append(numbers[5])
odd.append(numbers[6])
odd.append(numbers[7])
odd.append(numbers[9])
print(odd)