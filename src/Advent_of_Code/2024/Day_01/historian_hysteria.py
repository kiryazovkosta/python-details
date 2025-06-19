import os

def first(file_lines: list[str]) -> int:
    f = []
    s = []
    for line in file_lines:
        a, b = map(int, line.split())
        f.append(a)
        s.append(b)

    total_distance = 0
    f.sort()
    s.sort()
    for idx in range(0, len(f)):
        total_distance += abs(f[idx] - s[idx])

    return total_distance

def second(file_lines: list[str]) -> int:
    f = []
    s = {}
    for line in file_lines:
        a, b = map(int, line.split())
        f.append(a)
        if b in s:
            s[b] += 1
        else:
            s[b] = 1

    similarity_score = 0
    for idx in range(0, len(f)):
        similarity_score += f[idx] * s[f[idx]] if f[idx] in s else 0

    return similarity_score


def main():
    file_path = os.path.join(os.getcwd(), "input01.txt")
    with open(file_path, "r") as input_values_file:
        file_lines: list[str] = input_values_file.readlines()
        first_result = first(file_lines)
        print(first_result)
        second_result = second(file_lines)
        print(second_result)

if __name__ == "__main__":
    main()