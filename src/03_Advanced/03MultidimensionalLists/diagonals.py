size = int(input())
matrix = [[int(n) for n in input().split(", ")]for _ in range(size)]

diagonal = [matrix[i][i] for i in range(size)]
print(f"Primary diagonal: {', '.join(list(map(str, diagonal)))}. Sum: {sum(diagonal)}")

diagonal = [matrix[len(matrix) - 1 - i][i] for i in range(size - 1, - 1, -1)]
print(f"Secondary diagonal: {', '.join(list(map(str, diagonal)))}. Sum: {sum(diagonal)}")