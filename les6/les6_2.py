"""2
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

numbers = [1,2,3,3,2,1,5,4,5,17,6,6,9,8,11,123,29,5,-6,0]

def unique_numbers(nums):
    for element in nums:       # итерации по итерируемому обекту c типом данных "list"
        if nums.count(element) == 1: #если количество элементов со значением element равно 1 - значит элемент уникален
            yield element      # возвращаем генератор

for i in unique_numbers(numbers): # итерируем каждый элемент функции-генератора
    print(i, end=" ")