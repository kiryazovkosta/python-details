import os

def read_input(filename: str):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    file = open(file_path, 'r')
    return file

def close_input(file):
    file.close()