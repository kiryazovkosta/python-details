import os.path

FILE_PATH = "files/my_first_file.txt"

if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)

file = open(FILE_PATH, "x")
lines = [
    'I just created my first file1!\n',
    'I just created my first file2!\n',
    'I just created my first file3!\n',
    'I just created my first file4!\n',
    'I just created my first file5!\n']
file.writelines(lines)

new_text = 'Another text for writing'
file.write(new_text)