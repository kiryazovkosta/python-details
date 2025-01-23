rows, cols = [int(n) for n in input().split()]
m = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = -float("inf")
max_row_index = 0
max_col_index = 0
for i in range(len(m) - 2):
    for j in range(len(m[i]) - 2):
        current_sum = (
                m[i][j] + m[i][j+1] + m[i][j+2]
                + m[i+1][j] + m[i+1][j+1] + m[i+1][j+2]
                + m[i+2][j] + m[i+2][j+1] + m[i+2][j+2]
        )
        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = i
            max_col_index = j


print(f"Sum = {max_sum}")
sub_matrix = [m[row_index][max_col_index:max_col_index + 3] for row_index in range(max_row_index, max_row_index + 3)]
[print(*row) for row in sub_matrix]
