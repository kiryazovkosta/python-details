n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0
for index in range(len(matrix)):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)

sub_diagonal_sum = 0
for row_index in range(len(matrix) - 1, -1, -1):
    col_index = len(matrix) - 1 - row_index
    print(row_index)
    print(col_index)
    sub_diagonal_sum += matrix[row_index][col_index]
    print()
print(sub_diagonal_sum)