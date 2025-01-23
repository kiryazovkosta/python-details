SUCCESS = 0

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
searched_symbol = input()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_symbol:
            print(f"({row_index}, {col_index})")
            exit(SUCCESS)

print(f"{searched_symbol} does not occur in the matrix")