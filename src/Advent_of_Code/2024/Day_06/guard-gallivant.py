import os

def first(lines: list[str]):
    player = (0, 0)
    found_player: bool = False
    counter = set()
    matrix = []
    for rowIndex in range(len(lines)):
        matrix.append(list(lines[rowIndex].strip()))
        if not found_player:
            for colIndex in range(len(matrix[rowIndex])):
                if matrix[rowIndex][colIndex] == "^":
                    player = (rowIndex, colIndex)
                    matrix[rowIndex][colIndex] = "."
                    found_player = True

    commands = { "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1) }
    rotations = { "up": "right", "right": "down", "down": "left", "left": "up"  }

    current_command = "up"
    while True:
        next_position = (player[0] + commands[current_command][0], player[1] + commands[current_command][1])
        next_row, next_col = next_position[0], next_position[1]
        if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
            break

        if matrix[next_position[0]][next_position[1]] == ".":
            counter.add(next_position)
            player = next_position
        elif matrix[next_position[0]][next_position[1]] == "#":
            current_command = rotations[current_command]

    return len(counter)



def second(lines: list[str]) -> int:
    player = (0, 0)
    found_player: bool = False
    counter = 0
    current_counter = 0
    matrix = []
    for rowIndex in range(len(lines)):
        matrix.append(list(lines[rowIndex].strip()))
        if not found_player:
            for colIndex in range(len(matrix[rowIndex])):
                if matrix[rowIndex][colIndex] == "^":
                    player = (rowIndex, colIndex)
                    matrix[rowIndex][colIndex] = "."
                    found_player = True

    commands = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    rotations = {"up": "right", "right": "down", "down": "left", "left": "up"}

    current_command = "up"
    current_counter = 1
    while True:
        next_position = (player[0] + commands[current_command][0], player[1] + commands[current_command][1])
        next_row, next_col = next_position[0], next_position[1]
        if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
            break

        if matrix[next_position[0]][next_position[1]] == ".":
            player = next_position
        elif matrix[next_position[0]][next_position[1]] == "#":
            current_command = rotations[current_command]
            current_counter += 1
            if  current_counter == 4:
                counter += 1
                current_counter = 1

    return counter

def main():
    file_path = os.path.join(os.getcwd(), "input06.txt")
    with open(file_path, "r") as input_values_file:
        file_lines: list[str] = input_values_file.readlines()
        first_result = first(file_lines)
        print(first_result)
        second_result = second(file_lines)
        print(second_result)

if __name__ == "__main__":
    main()