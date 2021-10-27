from random import choice

def get_step() -> list[int, int]:
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
        return result


def chek_step(board: list[list], step: list[int, int]) -> bool:
    try:
        cell = board[step[0]][step[1]]
        if not cell:
            return True
    except IndexError:
        print("Неверные координаты")
    return False


def user_step(user: dict, board: list[list]):
    while True:
        step = get_step()
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            break
        else:
            print("Ячейка не существует или занята")
            continue


def possible_steps(board:list[list]):
    steps = []
    for idx_row, row in enumerate(board):
        steps.extend([[row.index(element), idx_row] for element in row if element == 0 ])
    return steps


def comp_step(user:dict, board:list[list]):
    step = choice(possible_steps(board))
    board[step[0]][step[1]] = user['symbol']
    return True


