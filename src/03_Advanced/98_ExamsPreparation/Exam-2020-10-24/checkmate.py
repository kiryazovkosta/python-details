SIZE = 8

board = []
queens = []
for row in range(SIZE):
    line = input().split()
    board.append(line)
    for col in range(SIZE):
        if board[row][col] == "Q":
            queens.append((row, col))

killers = []
for queen_row, queen_col in queens:
    found = False
    for index in range(queen_row+1, SIZE):
        if board[index][queen_col] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][queen_col] == "Q":
            break
    if found:
        continue

    for index in range(queen_row-1, -1, -1):
        if board[index][queen_col] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][queen_col] == "Q":
            break
    if found:
        continue

    for index in range(queen_col+1, SIZE):
        if board[queen_row][index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[queen_row][index] == "Q":
            break
    if found:
        continue

    for index in range(queen_col-1, -1, -1):
        if board[queen_row][index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[queen_row][index] == "Q":
            break
    if found:
        continue

    col_index = queen_col
    for index in range(queen_row + 1, SIZE):
        col_index += 1
        if col_index < 0 or col_index >= SIZE:
            break

        if board[index][col_index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][col_index] == "Q":
            break
    if found:
        continue

    col_index = queen_col
    for index in range(queen_row - 1, -1, -1):
        col_index += 1
        if col_index < 0 or col_index >= SIZE:
            break
        if board[index][col_index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][col_index] == "Q":
            break
    if found:
        continue

    col_index = queen_col
    for index in range(queen_row + 1, SIZE):
        col_index -= 1
        if col_index < 0 or col_index >= SIZE:
            break

        if board[index][col_index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][col_index] == "Q":
            break
    if found:
        continue

    col_index = queen_col
    for index in range(queen_row - 1, -1, -1):
        col_index -= 1
        if col_index < 0 or col_index >= SIZE:
            break
        if board[index][col_index] == "K":
            killers.append([queen_row, queen_col])
            found = True
            break
        elif board[index][col_index] == "Q":
            break
    if found:
        continue

if killers:
    for killer in killers:
        print(killer)
else:
    print("The king is safe!")