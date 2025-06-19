import os
import re

def first_second(content: str):
    total = 0
    enabled = True
    pattern = r"((?:do|don't|mul))\((?:(\d{1,3}),(\d{1,3}))?\)"
    matches = re.findall(pattern, content)
    for match in matches:
        (operation, first, second) = match
        if operation == "do":
            enabled = True
        elif operation == "don't":
            enabled = False
        else:
            if enabled:
                total += (int(first) * int(second))

    return total

def main():
    file_path = os.path.join(os.getcwd(), "input03.txt")
    with open(file_path, "r") as input_values_file:
        text: str = input_values_file.read()
        first_result = first_second(text)
        print(first_result)

if __name__ == "__main__":
    main()