import random

from homeworks.les12.board import Board


NAMES = (
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
)


class Player:

    def __init__(self, symbol, name=None):
        self.name = self._get_name(name)
        self.symbol = symbol

    def _get_name(self, name):
        if name:
            return name
        return random.choice(NAMES)

    def get_step(self, board: Board):
        return random.choice(tuple(board.free_cells()))


class Gamer(Player):

    def _get_name(self, name):
        if name:
            return name
        user_input = input("Введите ваше имя")
        return user_input

    def get_step(self, board: Board):
        while True:
            result = []
            input_step = input("Введите координаты хода через пробел\n")
            steps = input_step.split(" ")
            try:
                if len(steps) != 2:
                    raise ValueError
                for itm in steps:
                    result.append(int(itm))
            except ValueError:
                print("Ошибка ввода, повторите")
                continue
            return tuple(result)


board = Board(3)
user = Gamer("X")
user.get_step(board)
print(1)