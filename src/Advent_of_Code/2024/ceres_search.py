from utils import read_input, close_input

pattern = "XMAS"

matrix =  [list(line.strip()) for line in read_input("input04_test.txt").readlines()]

cols = len(matrix[0])
rows = len(matrix)

print("rows")
for row_idx in range(0, rows):
    for col_idx in range(0, cols):
        print(matrix[row_idx][col_idx])
    print("==========")

print("cols")
for col_idx in range(0, cols):
    for row_idx in range(0, rows):
        print(matrix[row_idx][col_idx])
    print("==========")

print("diagonal_topleft_to_bottomright_top")
for col_idx in range(0, cols):
    for row_idx in range(0, rows):
        print(matrix[row_idx][col_idx])
    print("==========")