n = int(input())

matrix = []
player_positions = []
health = 100
for row in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        player_positions = [row, line.index("P")]
        matrix[row][line.index("P")] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while True:
    move = input()
    new_row = player_positions[0] + moves[move][0]
    new_col = player_positions[1] + moves[move][1]
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        continue

    player_positions = [new_row, new_col]
    if matrix[new_row][new_col] == "H":
        health = min(health + 15, 100)
    elif matrix[new_row][new_col] == "X":
        print("Player escaped the maze. Danger passed!")
        break
    elif matrix[new_row][new_col] == "M":
        health = max(health - 40, 0)
        if health == 0:
            print("Player is dead. Maze over!")
            break
    matrix[new_row][new_col] = "-"

print(f"Player's health: {health} units")
matrix[player_positions[0]][player_positions[1]] = "P"
[print(''.join(row)) for row in matrix]


