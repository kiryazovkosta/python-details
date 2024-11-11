def check_rows(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col])

def check_cols(matrix):
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            print(matrix[row][col])

def check_diagonal(matrix):
    for index in range(len(matrix)):
        print(matrix[index][index])

    for index in range(len(matrix) - 1, -1, -1):
        print(matrix[len(matrix[0]) - index  -1][index])

def main():
    matrix = [[int(n) for n in input().split(" ")] for _ in range(3)]

if __name__ == "__main__":
    main()

