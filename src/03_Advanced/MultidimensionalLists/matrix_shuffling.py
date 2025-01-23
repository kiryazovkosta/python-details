VALID_ITEMS_COUNT = 5
VALID_COMMAND = 'swap'

def is_valid(array: [str], max_row: int, max_col: int) -> bool:
    if len(array) != VALID_ITEMS_COUNT:
        return False
    if array[0] != VALID_COMMAND:
        return  False

    coordinates = array[1:]
    try:
        coordinates = list(map(int, coordinates))
    except ValueError:
        return False

    if any(num < 0 for num in coordinates):
        return False
    return (
        coordinates[0] < max_row and coordinates[2] < max_row
        and coordinates[1] < max_col and coordinates[3] < max_col
    )

def print_matrix(matrix: [str]):
    [print(*row) for row in matrix]


rows, cols = [int(el) for el in input().split()]
m = [[el for el in input().split()] for _ in range(rows)]
command = ''
while True:
    command = input()
    if command == "END":
        break

    command = command.split()

    if is_valid(command, rows, cols):
        coord = [int(el) for el in command[1:]]
        m[coord[0]][coord[1]], m[coord[2]][coord[3]] = m[coord[2]][coord[3]], m[coord[0]][coord[1]]
        print_matrix(m)
    else:
        print("Invalid input!")
