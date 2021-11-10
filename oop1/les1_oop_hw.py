from random import randint

class Board:

    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size):
        self.size = size
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()
        self.signs_on_board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        col_numbers = "##" + "#".join(f"{item}" for item in range(self.size)) + "#"
        print(col_numbers)
        for idx, row in enumerate(self.signs_on_board):
            print(f'{idx}#{"|".join(f"{item}" for item in row)}#')
        print("#" * len(col_numbers))

    def add_step(self, step: tuple[int, int], sign = str):
        try:
            if step not in self.all_steps or step in self.done_steps:
                raise Exception
            self.done_steps.add(step)
            self.signs_on_board[step[0]][step[1]] = sign
            return True
        except Exception:
            print('Ячейка не существует или уже занята')
        return False

    def chek(self, sign) -> str:

        if len(self.done_steps) == self.size ** 2:
            return 'Ничья'

        self.diagonal = tuple(map(lambda idx: self.signs_on_board[idx][idx], range(0, self.size)))
        self.invert_diagonal = tuple(map(lambda idx: self.signs_on_board[idx][self.size - idx - 1], range(self.size - 1, -1, -1)))
        self.columns = (_ for _ in zip(*self.signs_on_board))
        self.rows = ( _ for _ in self.signs_on_board)

        def chek_line(line):
            line_set = set(line)
            if (0 not in line_set and len(line_set) == 1):
                raise ValueError("CHECK_LINE")
            return False

        try:
            _ = any(map(chek_line, (self.diagonal, self.invert_diagonal, *self.rows, *self.columns)))
        except ValueError as exc:
            if 'CHECK_LINE' in exc.args:
                return sign
            else:
                raise exc
        return None



created = Board(3)

created.print_board()
coord_x, coord_y = 1,1
created.add_step((coord_x,coord_y), 'X')
coord_x, coord_y =2,2
created.add_step((coord_x,coord_y), 'X')
coord_x, coord_y =0,0
created.add_step((coord_x,coord_y), 'X')
created.print_board()
print("Победа "+ created.chek("X"))