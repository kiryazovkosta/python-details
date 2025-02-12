n = int(input())

armor = 300
jet_position = []
matrix = []
enemy_counter = 4
for row in range(n):
    line = list(input())
    matrix.append(line)
    if "J" in line:
        jet_position = [row, line.index("J")]
        matrix[row][line.index("J")] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    move = input()
    row = jet_position[0] + moves[move][0]
    col = jet_position[1] + moves[move][1]
    if matrix[row][col] == "-":
        jet_position = [row, col]
    elif matrix[row][col] == "R":
        armor = 300
        jet_position = [row, col]
        matrix[row][col] = "-"
    elif matrix[row][col] == "E":

        matrix[row][col] = "-"
        enemy_counter -= 1
        jet_position = [row, col]
        if enemy_counter == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break

matrix[jet_position[0]][jet_position[1]] = "J"
[print(''.join(row)) for row in matrix]