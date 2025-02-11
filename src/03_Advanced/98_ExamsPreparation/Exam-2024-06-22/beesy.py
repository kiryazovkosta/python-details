n = int(input())

matrix = []
bee_position = []
energy = 15
nectar = 0
restore_energy = True

for row in range(n):
    line = list(input())
    matrix.append(line)
    if "B" in line:
        bee_position = [row, line.index("B")]
        matrix[row][line.index("B")] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    new_row = bee_position[0] + moves[command][0]
    new_col = bee_position[1] + moves[command][1]

    if new_row < 0:
        new_row = n - 1
    elif new_row >= n:
        new_row = 0

    if new_col < 0:
        new_col = n - 1
    elif new_col >= n:
        new_col = 0

    energy -= 1
    bee_position = [new_row, new_col]

    if matrix[new_row][new_col].isdigit():
        nectar += int(matrix[new_row][new_col])
    elif matrix[new_row][new_col] == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    matrix[new_row][new_col] = "-"

    if energy == 0:
        if nectar < 30 or restore_energy == False:
            print("This is the end! Beesy ran out of energy.")
            break
        else:
            energy = nectar - 30
            restore_energy = False


matrix[bee_position[0]][bee_position[1]] = "B"
[print(''.join(row)) for row in matrix]

