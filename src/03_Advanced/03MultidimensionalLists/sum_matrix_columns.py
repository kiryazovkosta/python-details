matrix = []
rows, cols = [int(n) for n in input().split(", ")]
for _ in range(rows):
    matrix.append([int(n) for n in input().split()])

for col_index in range(cols):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)