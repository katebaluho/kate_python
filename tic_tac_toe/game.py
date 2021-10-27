from itertools import cycle

from tic_tac_toe.board import get_board, board_match
from tic_tac_toe.steps import user_step
from tic_tac_toe.users import ask_mode, create_users


def game_init() -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    return {
        "users": create_users(ask_mode()),
        "board": get_board(3),
    }


def game_end():
    pass


def game_cycle(users: list[dict, ...], board: list[list]):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    for step_num, user in enumerate(cycle(users), 1):
        print(f"Ход Игрока: {user['name']}")
        user_step(user, board)
        if board_match(board):
            print(f"Победил {user['name']}")
            break
        if step_num >= 8:
            print("Ничья")
            break
    print("END GAME")


game_vars = game_init()
game_cycle(**game_vars)
