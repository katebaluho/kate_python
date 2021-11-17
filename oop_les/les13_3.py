import random


class SQMatrix:

    def __init__(self, data):
        self.size = len(data)
        self._data = data

    def __add__(self, other):
        if isinstance(other, SQMatrix):
            return self.__add__matrix__(other)
        elif isinstance(other, (int, float)):  # any((isinstance(other, int), isinstance(other, float)))
            return self.__add_digit__(other)

    def __add_digit__(self, num):
        result = [[i + num for i in itm] for itm in self._data]
        return SQMatrix(result)

    def __add__matrix__(self, matrix):
        return SQMatrix(
            [[sum(values) for values in zip(*pair)] for pair in zip(self._data, matrix._data)]
        )

    def __del__(self):
        print("Мне холодно БИЛЛИ")


matrix_1 = SQMatrix([[random.randint(1, 100) for _ in range(4)] for _ in range(4)])
matrix_2 = SQMatrix([[random.randint(1, 100) for _ in range(4)] for _ in range(4)])
matrix_3 = matrix_1 + matrix_2

# some = {matrix_1, matrix_2, matrix_3}

print(1)
# matrix_3 = matrix_1.__add__(matrix_2)