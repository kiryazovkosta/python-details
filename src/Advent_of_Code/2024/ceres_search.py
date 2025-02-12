from utils import read_input, close_input

pattern = "XMAS"

matrix =  [list(line.strip()) for line in read_input("input04.txt").readlines()]

cols = len(matrix[0])
rows = len(matrix)

counter = 0

print("rows")
for r in range(0, rows):
    for c in range(0, cols):
        if c <= cols - len(pattern):
            text = f"{matrix[r][c]}{matrix[r][c+1]}{matrix[r][c+2]}{matrix[r][c+3]}"
            if text == pattern:
                counter+=1

            # diagonal center - right-bottom
            if r <= rows - len(pattern):
                text = f"{matrix[r][c]}{matrix[r+1][c+1]}{matrix[r+2][c+2]}{matrix[r+3][c+3]}"
                if text == pattern:
                    counter += 1


        if c >= len(pattern) - 1:
            text = f"{matrix[r][c]}{matrix[r][c-1]}{matrix[r][c-2]}{matrix[r][c-3]}"
            if text == pattern:
                counter += 1

            # diagonal center - left-bottom
            if r <= rows - len(pattern):
                text = f"{matrix[r][c]}{matrix[r+1][c-1]}{matrix[r+2][c-2]}{matrix[r+3][c-3]}"
                if text == pattern:
                    counter += 1

print("cols")
for c in range(0, cols):
    for r in range(0, rows):
        if r <= rows - len(pattern):
            text = f"{matrix[r][c]}{matrix[r+1][c]}{matrix[r+2][c]}{matrix[r+3][c]}"
            if text == pattern:
                counter+=1

        if r >= len(pattern) - 1:
            text = f"{matrix[r][c]}{matrix[r-1][c]}{matrix[r-2][c]}{matrix[r-3][c]}"
            if text == pattern:
                counter += 1

            # diagonal center - right-top
            if c <= cols - len(pattern):
                text = f"{matrix[r][c]}{matrix[r-1][c+1]}{matrix[r-2][c+2]}{matrix[r-3][c+3]}"
                if text == pattern:
                    counter += 1

            if c >= len(pattern) - 1:
                text = f"{matrix[r][c]}{matrix[r-1][c-1]}{matrix[r-2][c-2]}{matrix[r-3][c-3]}"
                if text == pattern:
                    counter += 1


print(counter)