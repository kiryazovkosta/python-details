import os

def is_first_safe(levels: list[int]) -> bool:
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


def is_second_safe(levels: list[int]) -> bool:
    is_safe = True
    if levels[0] == levels[1]:
        return False
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

def first(lines: list[str])-> int:
    count = 0
    for line in lines:
        levels = [int(n) for n in line.split(" ")]
        if is_first_safe(levels):
            count += 1

    return count


def second(lines: list[str]) -> int:
    count = 0
    for line in lines:
        levels = [int(n) for n in line.split(" ")]
        if is_second_safe(levels):
            count += 1
        else:
            index = 0
            while index < len(levels):
                dampener = [item for idx, item in enumerate(levels) if idx != index]
                if is_second_safe(dampener):
                    count += 1
                    break
                index += 1

    return count

def main():
    file_path = os.path.join(os.getcwd(), "input02.txt")
    with open(file_path, "r") as input_values_file:
        file_lines: list[str] = input_values_file.readlines()
        first_result = first(file_lines)
        print(first_result)
        second_result = second(file_lines)
        print(second_result)

if __name__ == "__main__":
    main()