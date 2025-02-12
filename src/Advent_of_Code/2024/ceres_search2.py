from utils import read_input, close_input

pattern = "MAS"
counter = 0
m =  [list(line.strip()) for line in read_input("input04.txt").readlines()]
cols = len(m[0])
rows = len(m)
for r in range(1, rows - 1):
    for c in range(1, cols- 1):
        t1 = f"{m[r-1][c-1]}{m[r][c]}{m[r+1][c+1]}"
        t2 = f"{m[r+1][c+1]}{m[r][c]}{m[r-1][c-1]}"
        t3 = f"{m[r-1][c+1]}{m[r][c]}{m[r+1][c-1]}"
        t4 = f"{m[r+1][c-1]}{m[r][c]}{m[r-1][c+1]}"
        if (t1 == pattern or t2 == pattern) and (t3 == pattern or t4 == pattern):
            counter += 1
print(counter)