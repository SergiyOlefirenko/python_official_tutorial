matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix_transpose_rows_and_cols = [[row[i] for row in matrix] for i in range(4)]
print(f'{matrix} ==> {matrix_transpose_rows_and_cols}')

transposed = []
for i in range(len(matrix[0])):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# the same can be done with zip() function
transposed = list(zip(*matrix))
print(transposed)