def create_palindrome(row: int, col: int) -> str:
    x = chr(ord('a') + row)
    y = chr(ord('a') + row + col)
    return f"{x}{y}{x}"

rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([])
for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index].append(create_palindrome(row_index, col_index))

[print(*row) for row in matrix]