def print_board(matrix: []) -> None:
    for row_index in range(len(matrix)):
        print(''.join(matrix[row_index]))

def main():
    rows, columns = [int(n) for n in input().split(", ")]
    player_row, player_col = -1, -1
    board = []
    for row_index in range(rows):
        board.append(list(input()))
        for col_index in range(columns):
            if board[row_index][col_index] == "C":
                player_row = row_index
                player_col = col_index

    commands = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }

    seconds = 16
    while seconds > 0:
        command = input()
        if command == "defuse":
            if board[player_row][player_col] != "B":
                seconds -= 2
            else:
                seconds -= 4
                if seconds >= 0:
                    board[player_row][player_col] = "D"
                else:
                    board[player_row][player_col] = "X"
                break
        else:
            r, y = commands[command]
            new_row_index =  + player_row + r
            new_col_index = commands[command][1] + player_col

            if 0 <= new_row_index < rows and 0 <= new_col_index < columns:
                if board[new_row_index][new_col_index] == "*":
                    if not board[player_row][player_col] == "B":
                        board[player_row][player_col] = "*"
                    board[new_row_index][new_col_index] = "C"
                    player_row = new_row_index
                    player_col = new_col_index
                elif board[new_row_index][new_col_index] == "B":
                    board[player_row][player_col] = "*"
                    player_row = new_row_index
                    player_col = new_col_index
                elif board[new_row_index][new_col_index] == "T":
                    board[player_row][player_col] = "*"
                    board[new_row_index][new_col_index] = "*"
                    break

        print_board(board)

    print_board(board)

if __name__ == "__main__":
    main()