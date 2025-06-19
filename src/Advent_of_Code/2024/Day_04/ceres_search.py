import os

def first(lines: list[str]) -> int:
    pattern = "XMAS"

    matrix = [list(line.strip()) for line in lines]
    cols = len(matrix[0])
    rows = len(matrix)

    counter = 0
    for r in range(0, rows):
        for c in range(0, cols):
            if c <= cols - len(pattern):
                text = f"{matrix[r][c]}{matrix[r][c + 1]}{matrix[r][c + 2]}{matrix[r][c + 3]}"
                if text == pattern:
                    counter += 1

                if r <= rows - len(pattern):
                    text = f"{matrix[r][c]}{matrix[r + 1][c + 1]}{matrix[r + 2][c + 2]}{matrix[r + 3][c + 3]}"
                    if text == pattern:
                        counter += 1

            if c >= len(pattern) - 1:
                text = f"{matrix[r][c]}{matrix[r][c - 1]}{matrix[r][c - 2]}{matrix[r][c - 3]}"
                if text == pattern:
                    counter += 1

                if r <= rows - len(pattern):
                    text = f"{matrix[r][c]}{matrix[r + 1][c - 1]}{matrix[r + 2][c - 2]}{matrix[r + 3][c - 3]}"
                    if text == pattern:
                        counter += 1

    for c in range(0, cols):
        for r in range(0, rows):
            if r <= rows - len(pattern):
                text = f"{matrix[r][c]}{matrix[r + 1][c]}{matrix[r + 2][c]}{matrix[r + 3][c]}"
                if text == pattern:
                    counter += 1

            if r >= len(pattern) - 1:
                text = f"{matrix[r][c]}{matrix[r - 1][c]}{matrix[r - 2][c]}{matrix[r - 3][c]}"
                if text == pattern:
                    counter += 1

                if c <= cols - len(pattern):
                    text = f"{matrix[r][c]}{matrix[r - 1][c + 1]}{matrix[r - 2][c + 2]}{matrix[r - 3][c + 3]}"
                    if text == pattern:
                        counter += 1

                if c >= len(pattern) - 1:
                    text = f"{matrix[r][c]}{matrix[r - 1][c - 1]}{matrix[r - 2][c - 2]}{matrix[r - 3][c - 3]}"
                    if text == pattern:
                        counter += 1
    return counter

def second(lines: list[str]) -> int:
    pattern = "MAS"
    counter = 0
    m = [list(line.strip()) for line in lines]
    cols = len(m[0])
    rows = len(m)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            t1 = f"{m[r - 1][c - 1]}{m[r][c]}{m[r + 1][c + 1]}"
            t2 = f"{m[r + 1][c + 1]}{m[r][c]}{m[r - 1][c - 1]}"
            t3 = f"{m[r - 1][c + 1]}{m[r][c]}{m[r + 1][c - 1]}"
            t4 = f"{m[r + 1][c - 1]}{m[r][c]}{m[r - 1][c + 1]}"
            if (t1 == pattern or t2 == pattern) and (t3 == pattern or t4 == pattern):
                counter += 1
    return counter

def main():
    file_path = os.path.join(os.getcwd(), "input04.txt")
    with open(file_path, "r") as input_values_file:
        file_lines: list[str] = input_values_file.readlines()
        first_result = first(file_lines)
        print(first_result)
        second_result = second(file_lines)
        print(second_result)

if __name__ == "__main__":
    main()