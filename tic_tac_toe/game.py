from itertools import cycle
from constants import END_GAME
from tic_tac_toe.board import get_board, board_match, print_board, draw_match_board
from tic_tac_toe.steps import user_step, comp_step
from tic_tac_toe.users import ask_mode, create_users

MODES_STEP = {
    "COMP": {"get_step": comp_step},
    "USER": {"get_step": user_step},
}

def game_init(**kwargs) -> dict:
    print("Добро пожаловать в Игру Крестики Нолики")
    return {
        "users": create_users(ask_mode(), **kwargs),
        "board": get_board(3),
    }


def game_end():
    while True:
        user_answer = input(f'Начать новую игру? {END_GAME}')
        if not user_answer.upper() in END_GAME:
            print("Неверный выбор.Попробуйте еще раз.")
        else:
            return False if user_answer == END_GAME[0] else True


def game_cycle(users: list[dict, ...], board: list[list]):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    for step_num, user in enumerate(cycle(users), 1):
        print_board(board)
        print(f"Ход Игрока: {user['name']}")
        MODES_STEP[user['mode']]['get_step'](user, board)
        #user_step(user, board)
        if board_match(board):
            print(f"Победил {user['name']}")
            break
        if draw_match_board(step_num, board):
            print("Ничья")
            break


