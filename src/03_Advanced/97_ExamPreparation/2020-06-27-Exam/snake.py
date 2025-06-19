def main():
    size = int(input())
    matrix = []

    s = [0, 0]
    b1 = [0, 0]
    b2 = [0, 0]
    f_b = True
    food = 0

    for rowIndex in range(size):
        line = list(input())
        matrix.append(line)
        for colIndex in range(len(line)):
            if matrix[rowIndex][colIndex] == "S":
                s = [rowIndex, colIndex]
            if matrix[rowIndex][colIndex] == "B":
                if f_b:
                    b1 = [rowIndex, colIndex]
                    f_b = False
                else:
                    b2 = [rowIndex, colIndex]

    moves = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }

    while food < 10:
        command = input()
        m_p = moves[command]
        s_n = s[0] + m_p[]

if __name__ == "__main__":
    main()