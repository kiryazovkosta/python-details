matrix = []
sum_elements = 0
row_count, col_count = (int(x) for x in input().split(", "))
for row_index in range(row_count):
    data_row = [int(el) for el in input().split(", ")]
    sum_elements += sum(data_row)
    matrix.append(data_row)

print(sum_elements)
print(matrix)