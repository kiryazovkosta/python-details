import os

def read_input(filename: str) -> list[str]:
    content: list[str] = []
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = [line.strip() for line in file.readlines()]

    return content
