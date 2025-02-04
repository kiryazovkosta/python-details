matrix = []
rows = int(input())
for _ in range(rows):
    matrix.append([int(n) for n in input().split(", ") if int(n) % 2 == 0])
print(matrix)