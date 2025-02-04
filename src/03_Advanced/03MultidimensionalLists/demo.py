# array = [
#     [1, 2],
#     [3, 4, 5, 6],
#     [7, 8, 9]
# ]
#
# # for row_index in range(len(array)):
# #     for col_index in range(len(array[row_index])):
# #         print(array[row_index][col_index])
#
# counter = 0
# matrix = []
# for row_index in range(3):
#     matrix.append([])
#     for col_index in range(2):
#         counter += 1
#         matrix[row_index].append(counter)
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index], sep= " ")
#     print()
import sys


# print([[int(n) for n in input().split(", ") if int(n) % 2 == 0] for fow in range(int(input()))])
# # flatten_matrix = [n for row in matrix for n in row]
# # print(flatten_matrix)

# matrix = [[1,2,3],[4,5,6]]
# for row in matrix:
#     for el in row:
#         print(el)
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index], end=" ")
#     print()

matrix = []
rows, cols = [int(n) for n in input().split(", ")]
for _ in range(rows):
    matrix.append([int(n) for n in input().split()])

sums = [cols] * 6
print(sums)
for row in matrix:
    for index in range(cols):
        sums[index] += row[index]
print(sums)

