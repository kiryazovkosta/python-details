import os

def read_input(filename: str, strip: bool = True) -> list[str]:
    '''
    Read text file and returns all lines as list of strings
    '''
    content: list[str] = []
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    if strip:
        content = [line.strip() for line in content]

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

def print_matrix(matrix, delimiter) -> None:
    for row in range(len(matrix)):
        print(delimiter.join(matrix[row]))
