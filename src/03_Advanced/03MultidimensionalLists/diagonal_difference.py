size = int(input())
matrix = [[int(n) for n in input().split()]for _ in range(size)]

primary_diagonal_sum = sum([matrix[i][i] for i in range(size)])
secondary_diagonal_sum = sum([matrix[len(matrix) - 1 - i][i] for i in range(size - 1, - 1, -1)])
print((abs(primary_diagonal_sum - secondary_diagonal_sum)))