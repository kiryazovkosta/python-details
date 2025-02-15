matrix = []
rows = int(input())
for _ in range(rows):
    matrix.append([int(n) for n in input().split(", ")])

flatten_matrix = [n for row in matrix for n in row]
print(flatten_matrix)
