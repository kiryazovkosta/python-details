letter = list(input())
n = int(input())
matrix = []
p = []
for row in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        p = [row, line.index("P")]
        matrix[row][line.index("P")] = "-"
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
move_count = int(input())
while move_count > 0:
    move_count -= 1
    m = moves[input()]
    nr = p[0] + m[0]
    nc = p[1] + m[1]
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        if letter:
            letter.pop()
            continue

    if matrix[nr][nc].isalpha():
        letter.append(matrix[nr][nc])
        matrix[nr][nc] = "-"
    p = [nr, nc]

matrix[p[0]][p[1]] = "P"
print(''.join(letter))
[print(''.join(row)) for row in matrix]


