import os

def read_input(filename: str) -> list[str]:
    '''
    Read text file and returns all lines as list of strings
    '''
    content: list[str] = []
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = [line.strip() for line in file.readlines()]

    return content

def read_single(filename: str) -> str:
    '''
    Read text file and returns content as single string
    '''
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readline().strip()

    return content
