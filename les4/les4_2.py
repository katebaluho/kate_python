"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

# matrix1 = [
#     [6,1,1],
#     [3,6,3],
#     [4,4,6]
# ]
#
# matrix2 = [
#     [1,2,2],
#     [5,1,5],
#     [7,7,1]
# ]

count_rows_matrix1 = input('Enter the numbers of rows of the matrix A: ')
count_columns_matrix = input('Enter the numbers of columns of the matrix A and B: ')
count_rows_matrix1 = input('Enter the numbers of rows of the matrix B: ')

matrix1



result = []
for rows in matrix1:
    new_row = []
    for column in zip(*matrix2):
        new_elements = []

        for element1, element2 in zip(rows, list(column)):
            new_elements.append(element1*element2)

        new_row.append(sum(new_elements))
    result.append(new_row)
print(result)


