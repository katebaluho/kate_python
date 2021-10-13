
from random import randint
"""
Имеется 2 кортежа с координатами Ферзя и Пешки на шахматной доске
Определить Бьет ли Ферзь пешку
координаты хранятся (x, y)
"""

queen = (5,4)
pawn = (5,2)

chess_row = 8
chess_col = 8
result = "Пешка в безопасности"

#check vertical and gorizontal
if queen[1] == pawn[1] or queen[0] == pawn[0]:
    result = "Ферзь бьет пешку"
else:
#check diagonals
#диагонали поля это графики ф-ций y = x+n и y=-x+m
#по сути проверка одинаковый ли сдвиг от главной диагонали
    x_queen_shift = queen[1]-queen[0]
    x2_queen_shift = queen[1]+queen[0]

    x_pawn_shift = pawn[1]-pawn[0]
    x2_pawn_shift = pawn[1]+pawn[0]
    if(
        x_queen_shift == x_pawn_shift or
        x_queen_shift == x2_pawn_shift or
        x2_queen_shift == x_pawn_shift or
        x2_queen_shift == x2_pawn_shift
    ):
        result = "Ферзь бьет пешку"

print(result)
