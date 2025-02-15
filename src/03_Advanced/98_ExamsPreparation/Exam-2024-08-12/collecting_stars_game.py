INITIAL_VALUE = 2
STEP = 1
MIN_VALUE = 0
MAX_VALUE = 10
ONE = 1
ZERO = 0
PLAYER_SYMBOL = "P"
STAR_SYMBOL = "*"
WALL_SYMBOL = "#"
NONE_SYMBOL = "."
SPACE_SYMBOL = " "

def main():
    n = int(input())

    stars = INITIAL_VALUE
    matrix = []
    player_position = []

    for row in range(n):
        line = input().split(SPACE_SYMBOL)
        matrix.append(line)
        if PLAYER_SYMBOL in line:
            player_position = [row, line.index(PLAYER_SYMBOL)]
            matrix[row][line.index(PLAYER_SYMBOL)] = NONE_SYMBOL

    moves = {
        "up": (-ONE, ZERO),
        "down": (ONE, ZERO),
        "left": (ZERO, -ONE),
        "right": (ZERO, ONE)
    }

    while MIN_VALUE < stars < MAX_VALUE:
        command = input()
        next_row = moves[command][ZERO] + player_position[ZERO]
        next_col = moves[command][ONE] + player_position[ONE]
        if not(ZERO <= next_row < n and ZERO <= next_col < n):
            next_row = ZERO
            next_col = ZERO

        if matrix[next_row][next_col] == STAR_SYMBOL:
            stars += STEP
            matrix[next_row][next_col] = NONE_SYMBOL
        elif matrix[next_row][next_col] == WALL_SYMBOL:
            stars -= STEP
            continue

        player_position = [next_row, next_col]

    if stars == MAX_VALUE:
        print("You won! You have collected 10 stars.")
    else:
        print("Game over! You are out of any stars.")

    print(f"Your final position is [{player_position[ZERO]}, {player_position[ONE]}]")
    matrix[player_position[ZERO]][player_position[ONE]] = PLAYER_SYMBOL
    [print(SPACE_SYMBOL.join(row)) for row in matrix]

if __name__ == "__main__":
    main()