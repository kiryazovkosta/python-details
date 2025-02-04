rows, cols = [int(n) for n in input().split()]
matrix = [[el for el in input().split()]for _ in range(rows)]

counter = 0
for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        if (
                matrix[row_index][col_index] == matrix[row_index][col_index + 1]
                and matrix[row_index][col_index] == matrix[row_index+1][col_index]
                and matrix[row_index][col_index] == matrix[row_index + 1][col_index + 1]
        ):
            counter += 1

print(counter)