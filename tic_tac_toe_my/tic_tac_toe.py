"""
Игра Крестики нолики
"""
"""
Правила игры:
Игровое поле 3х3
участвуют 2 игрока
игроки ходят поочереди
каждый игрок имеет индивидуальный символ который ставит на свободную ячейку игрового поля
Победитель определяется по следующим правилам:
символ игрока заполняет горизонталь, вертикаль или диагональ
возможный исход игры когда нет победителя
"""
# Играть с компуктером
# Игровое поле в виде Матрицы 3на3 не изменяемо.
# Ячейка игрового поля будет изменяться,
"""(
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)"""
#  Игрок Словарь - ТИП пользователя

# Управляющий игрой распорядитель

# Функция матчинга игрового поля на наличие победителя
# Определение возможности хода
# Функция Взаимодействия с пользователем на предмет хода
# Функция совершения хода записывает на игровое поле в ячейку самого пользователя

from itertools import cycle
from random import randint

interface_string = {
    "rules": "",
    "hello": "Здравствуй игрок!",
    "enter_name": "Игрок #{user_number}: Введите свое имя  ",
    "game_type": "С кем вы желаете играть {variants}   ",
    "ask_step_user": "Ход #{step_number} игрока {name} символом {sign}. Введите число от 1 до 9:  ",
    "step_computer": "Ход #{step_number} Компьютера символом {sign}. Компьютер ходит на ячейку {cell}.\n Нажмите Enter.",
    "win": "Победил игрок {name} на ходу #{step_number}.\n Нажмите Enter.",
    "new_game": "Желаете начать новую игру? {variants}  ",
    "draw": "Ничья! Победителей нет."
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "ask_step_user": lambda template, **kwargs: template.format(**kwargs),
    "step_computer": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}
#тип хода
move_type = {
    "U": lambda *args: choise_human(*args),
    "C": lambda *args: choise_of_computer(*args)
}

#возвращает строку для пользователя в зависимости от переданного шаблона и агрументов
def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])

#Возвращает true если есть победитель, иначе false
def matrix_match(board):
    def chek_line(line):
        line_set = set(line)
        if ("*" not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False

#Выводит на печать доску
def print_board(board):
    for row in board:
        print(*row, sep=' | ')
        print("-"*10)

#проверка хода и запись в ячейку символа Х или Y
def check_cell(cell, player_sign, board):
    index_row = (cell-1)//len(board)
    index_element  = (cell-1)-len(board)*index_row
    if board[index_row][index_element] == '*':
        board[index_row][index_element] = player_sign
        return True
    return False

#ход человека
def choise_human( counter_steps, player:tuple , board):

    player_name, player_sign = player
    while True:
        try:
            str_cell = user_interface("ask_step_user", step_number = counter_steps, sign = player_sign,name = player_name)
            number_cell = int(str_cell)
            if not (1<= number_cell <= 9):
                raise ValueError
            elif not check_cell(number_cell, player_sign, board):
                raise AssertionError
        except ValueError:
            print("Введите число от 1 до 9.")
        except AssertionError:
            print("Попробуйте сделать другой выбор. Эта ячейка уже занята.")
        else:
            return number_cell
    return False

#ход компьютера
def choise_of_computer(counter_steps, board):

    #определяем "линии" для поиска
    board_len = len(board)
    diagonal = list(map(lambda idx: board[idx][idx], range(0, board_len)))
    # diagonal_invert = list(map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1)))
    diagonal_invert = list(map(lambda idx: board[idx][board_len - idx - 1], range(board_len)))

    #проверяем наличие 2 символов
    def find_two_symbols(line, sign):
        return True if list(line).count(sign) == 2  and ('*' in line) else False

    #выражения для вычисления порядкового номера
    calculate_number_cell = {
        'diagonal': lambda idx_row: idx_row*(len(board)+1)+1,
        'diagonal_invert':  lambda idx_row: (len(board)-1)*(idx_row+1)+1,            #lambda idx_row: (len(board)-1)*(idx_row+1)+1,
        'row': lambda idx_row,idx_element: idx_row * len(board)+idx_element+1,
        'col': lambda idx_row,idx_element: idx_row + len(board)*idx_element+1
    }
    
    number_cell = None

    def control_cell(sign):
        cell = None
        if find_two_symbols(diagonal, sign):
            cell = calculate_number_cell['diagonal'](diagonal.index('*'))
        elif find_two_symbols(diagonal_invert, sign):
            cell = calculate_number_cell['diagonal_invert'](diagonal_invert.index('*'))
        else:
            for idx_row, row, col in zip(range(len(board)), board, zip(*board)):
                if find_two_symbols(row, sign):
                    cell = calculate_number_cell['row'](idx_row, row.index('*'))
                    break
                if find_two_symbols(col, sign):
                    cell = calculate_number_cell['col'](idx_row, col.index('*'))
                    break
        return cell

    # Сначала проверям возсожна ли победа, если нет блокируем соперника
    number_cell = control_cell("0")  or control_cell("X")

    #если и здесь ход не совершен, и переменная None, значит генерируем рандом.
    create_moove = True if number_cell else False
    while not create_moove:
        number_cell = randint(1,9)
        create_moove = check_cell(number_cell, "0", board) #проверяе рандом и записываем когда находим свободную ячейку
    else:
        check_cell(number_cell, "0", board)
        user_interface("step_computer", step_number=counter_steps, sign="0", cell=number_cell)
        return number_cell

#Проверяем ввод значений для выбора
def choice_valid_answer(ask_key, answer_str):
    while True:
        value = user_interface(ask_key).upper()
        if not value in answer_str:
            print("Введите верное значение!")
        else:
            return value

# 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
# Опрашивать пользователя на предмет хода
# Проверяем возможность хода
# Проверяем выйгрышный вариант
# Либо поздравить с победой, либо обьявить Ничью

def game(player_info, board):

    player_pool = cycle(player_info)
    all_movies = []

    #циклическая итерация по пользователям
    for counter_steps, player in enumerate(player_pool, start=1):
        print_board(board)  # показываем доску
        name_player,_ = player

        if name_player == "Computer":
            all_movies.append(move_type["C"](counter_steps, board))  # ХОД КОМПЬЮТЕРА
        else:
            all_movies.append(move_type["U"](counter_steps, player, board))  # ХОД ЧЕЛОВЕКА

        print(all_movies)

        if matrix_match(board):
            user_interface('win', name = name_player, step_number = counter_steps//2)
            break
        if len(all_movies) == len(board)**2:
            user_interface('draw')
            break
    print("===ИТОГ===")
    print_board(board)

def main():
    user_interface("hello")

    while True:
        game_type_choise = choice_valid_answer('game_type', ("U", "C"))  # выбор типа игры

        player_info = ((user_interface("enter_name", user_number=1), "X"),
                       ((user_interface("enter_name", user_number=2) if game_type_choise == "U" else "Computer"), "0"))

        game(player_info, (['*', '*', '*'],
                          ['*', '*', '*'],
                          ['*', '*', '*']))
        if choice_valid_answer('new_game', ("Y", "N")) == "N":
            print("Спасибо за игру. Возвращайтесь!")
            break
    return 1

main()