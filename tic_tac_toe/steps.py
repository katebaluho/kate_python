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