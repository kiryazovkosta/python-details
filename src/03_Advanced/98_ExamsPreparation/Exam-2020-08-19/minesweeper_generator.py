coordinates = [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, 1),(1, 1),(-1, -1), (1, -1)]

n = int(input())
b = int(input())
board = []
[board.append(['0' for _ in range(n)]) for _ in range(n)]

bombs = []
for _ in range(b):
    bomb_location = list(map(int, input()[1:-1].split(", ")))
    bombs.append((bomb_location[0], bomb_location[1]))
    for coordinate in coordinates:
        new_row = coordinate[0] + bomb_location[0]
        new_col = coordinate[1] + bomb_location[1]
        if 0 <= new_row < n and 0<= new_col < n:
            new_value = int(board[new_row][new_col]) + 1
            board[new_row][new_col] = str(new_value)

for b in bombs:
    board[b[0]][b[1]] = '*'

[print(' '.join(map(str,row))) for row in board]

