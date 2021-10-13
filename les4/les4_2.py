from random import randint
"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""
count_rows_matrix1 = int(input('Enter the numbers of rows of the matrix A: '))
count_columns_matrix1 = int(input('Enter the numbers of columns of the matrix A: '))
count_rows_matrix2 = count_columns_matrix1
count_columns_matrix2 = int(input('Enter the numbers of rows of the matrix B: '))
#заполняем, чтобы было интереснее
matrix1 = []
for id_of_row in range(count_rows_matrix1):
    row = []  
    for element in range(count_columns_matrix1):
        row.append(randint(1,15))
    matrix1.append(row)
print(matrix1)

matrix2 = []
for id_of_row in range(count_rows_matrix2):
    row = []  
    for element in range(count_columns_matrix2):
        row.append(randint(15,25))
    matrix2.append(row)
print(matrix2)

# умножаем
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

# test
# [[3, 7, 5], [3, 10, 3]]
# [[23, 16, 24, 23], [18, 23, 16, 24], [23, 24, 21, 20]]
# [[310, 329, 289, 337], [318, 350, 295, 369]]
