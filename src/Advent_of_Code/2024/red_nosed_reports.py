import os

def read_input(filename: str):
    current_directory = os.path.join(os.getcwd(), "src/Advent_of_Code/2024")
    file_path = os.path.join(current_directory, "input02.txt")
    file = open(file_path, 'r')
    return file

def close_input(file):
    file.close()

def is_safe(levels: list[int]) -> bool:
    is_safe = True
    order = 'asc' if levels[0] < levels[1] else 'desc'
    for idx in range(0, len(levels) - 1):
        diff = levels[idx] - levels[idx + 1]
        if abs(diff) == 0 or abs(diff) > 3:
            is_safe = False
            break
        
        if levels[idx] > levels[idx + 1] and order == "asc":
            is_safe = False
            break

        if levels[idx] < levels[idx + 1] and order == "desc":
            is_safe = False
            break

    return is_safe

def main():
    file = read_input("input02.txt")
    count = 0
    for line in file.readlines():
        levels = [int(n) for n in line.split(" ")]
        if is_safe(levels):
            count += 1
    
    print(count)
    close_input(file)

if __name__ == "__main__":
    main()