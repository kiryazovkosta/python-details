def print_matrix(matrix: [], delimiter: str) -> None:
    for row in range(len(matrix)):
        print(delimiter.join(matrix[row]))

n = int(input())

units = 100
ship_row, ship_col = 0, 0

space = []
for row_index in range(n):
    space.append(input().split(" "))
    for col_index in range(n):
        if space[row_index][col_index] == "S":
            ship_row, ship_col = row_index, col_index

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

space[ship_row][ship_col] = "."
while True:
    command = input()
    units -= 5
    ship_new_row, ship_new_col = commands[command][0] + ship_row, commands[command][1] + ship_col

    if ship_new_row < 0 or ship_new_row >= n or ship_new_col < 0 or ship_new_col >= n:
        print("Mission failed! The spaceship was lost in space.")
        break

    if space[ship_new_row][ship_new_col] == "R":
        units = min(units + 10, 100)
    elif space[ship_new_row][ship_new_col] == "M":
        units -= 5
        space[ship_new_row][ship_new_col] = "."

    ship_row, ship_col = ship_new_row, ship_new_col

    if space[ship_row][ship_col] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {units} resources left.")
        break

    if units < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

if space[ship_row][ship_col] != "P":
    space[ship_row][ship_col] = "S"

print_matrix(space, " ")


