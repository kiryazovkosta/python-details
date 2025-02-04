def spread_rabbits(game_board: list[[]], rabbits_positions: set):
    new_rabbit_positions = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for rab_row, rab_col in rabbits_positions:
        for d_row, d_col in directions:
            new_row, new_col = rab_row + d_row, rab_col + d_col
            if new_row < 0 or new_row >= len(game_board) or new_col < 0 or new_col >= len(game_board[0]):
                continue
            game_board[new_row][new_col] = "B"
            new_rabbit_positions.add((new_row, new_col))

    return game_board, rabbits_positions.union(new_rabbit_positions)

rows, cols = [int(el) for el in input().split()]

board = []

player_row_index, player_col_index = 0, 0
has_won = False
has_lost = False
rabbits = set() # {(1, 3), (4, 0)}

moves = {
    "R": lambda r, c: (r, c + 1),
    "L": lambda r, c: (r, c - 1),
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
}

for row in range(rows):
    board.append(list(input()))
    for col in range(cols):
        if board[row][col] == "P":
            player_row_index = row
            player_col_index = col
        elif board[row][col] == "B":
            rabbits.add((row, col))

operations = list(input()) #"R", "L", "U", "D

for operation in operations:
    player_new_row_index, player_new_col_index = moves[operation](player_row_index, player_col_index)
    board, rabbits = spread_rabbits(board, rabbits)
    if (player_row_index, player_col_index) not in rabbits:
        board[player_row_index][player_col_index] = "."
    if (
        player_new_row_index < 0 or player_new_row_index >= rows
            or player_new_col_index < 0 or player_new_col_index >= cols
    ):
        has_won = True
        break
    player_row_index, player_col_index = player_new_row_index, player_new_col_index
    if board[player_row_index][player_col_index] == "B":
        has_lost = True
        break

for row in board:
    print("".join(row))

if has_won:
    print(f"won: {player_row_index} {player_col_index}")
elif has_lost:
    print(f"dead: {player_row_index} {player_col_index}")


