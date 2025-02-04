rows, cols = [int(n) for n in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sub_matrix_sum = 0
max_sub_matrix_row_index = 0
max_sub_matrix_col_index = 0
for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        down_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        sub_matrix_sum = current_element + next_element + down_element + diagonal_element
        if sub_matrix_sum > max_sub_matrix_sum:
            max_sub_matrix_sum = sub_matrix_sum
            max_sub_matrix_row_index = row_index
            max_sub_matrix_col_index = col_index

for row_index in range(max_sub_matrix_row_index, max_sub_matrix_row_index + 2):
    print(f"{matrix[row_index][max_sub_matrix_col_index]} {matrix[row_index][max_sub_matrix_col_index + 1]}")
print(max_sub_matrix_sum)

