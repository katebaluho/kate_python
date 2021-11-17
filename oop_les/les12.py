import random

from tic_tac_toe import board


class Human:
    __population = []

    def __init__(self, name, sex, skin):
        self.name = name
        self.sex = sex
        self.skin = skin
        self.age = 0
        Human.__population.append(self)

    def say(self):
        print("HELLO MY NAME IS", self.name)

    def reproduction(self, other: "Human") -> "Human":
        name = "SOME_NEW_NAME"
        sex = random.choice((self.sex, other.sex))
        skin = random.choice((self.skin, other.skin))
        return other.__class__(name, sex, skin)

    def population_count(self) -> int:
        return len(self.__population)

    def population(self):
        return tuple(self.__population)


"""
1. Инкапсуляция
2. Наследование
3. Полиморфизм
"""

"""
СОКРЫТИЕ Уровни доступа
1. Public
2. Protected
3. Private
"""


class Board:

    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг


    def __init__(self, size):
        self.size = size
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()
        self._protected = 1111
        self.__private = 22222

    def print_board(self):
        pass

    def add_step(self, step: tuple[int, int]):
        pass

    def chek(self) -> bool:
        pass


class Animal:

    def __init__(self, color: str):
        self.color = color

    def some(self):
        print("some my color", self.color)


class Wolf(Animal):

    def __init__(self, height, breed, color: str):
        self.height = height
        self.breed = breed
        # self.color = color
        super().__init__(color)

    def say(self):
        print("РРРРРРР")


class Dog(Wolf):

    def wof(self):
        print("Wof")

    def say(self):
        print("Гаф")
        super().say()


wolf = Wolf(123, "Саблезубый волк", "Черный")
dog = Dog(123, "Шпиц", "Белый")
print(1)
