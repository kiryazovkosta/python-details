from collections import deque

rows, cols = [int(el) for el in input().split()]
text = deque(input())

matrix = []

[matrix.append([""] * cols) for _ in range(rows)]

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if row_index % 2 == 0:
            matrix[row_index][col_index] = text[0]
        else:
            matrix[row_index][-1 - col_index] = text[0]
        text.rotate(-1)

[print(*row, sep="") for row in matrix]
