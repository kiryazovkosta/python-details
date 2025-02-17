n = int(input())

snake = []
burrows = []
foods = 0

matrix = []
for row in range(n):
    line = list(input())
    matrix.append(line)
    for col in range(n):
        if matrix[row][col] == "S":
            snake = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "B":
            burrows.append([row, col])

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    new_row = moves[command][0] + snake[0]
    new_col = moves[command][1] + snake[1]
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        print("Game over!")
        break

    if matrix[new_row][new_col] == "*":
        foods += 1
        snake = [new_row, new_col]
        matrix[new_row][new_col] = "."
        if foods >= 10:
            print("You won! You fed the snake.")
            matrix[new_row][new_col] = "S"
            break
    elif matrix[new_row][new_col] == "B":
        if new_row == burrows[0][0] and new_col == burrows[0][1]:
            snake = [burrows[1][0], burrows[1][1]]
            matrix[new_row][new_col] = "."
            matrix[burrows[1][0]][burrows[1][1]] = "."
        elif new_row == burrows[1][0] and new_col == burrows[1][1]:
            snake = [burrows[0][0], burrows[0][1]]
            matrix[new_row][new_col] = "."
            matrix[burrows[0][0]][burrows[0][1]] = "."
    else:
        snake = [new_row, new_col]
        matrix[new_row][new_col] = "."

print(f"Food eaten: {foods}")
for row in matrix:
    print(''.join(row))



