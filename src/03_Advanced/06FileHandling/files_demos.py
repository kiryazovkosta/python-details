import os

# file = open("files/_example.txt", 'r')
# result = file.read()
#
# print(result)

current_dir = os.curdir
filename = "numbers.txt"
file_path = os.path.join(current_dir, "files", filename)
print(file_path)
file = open(file_path, "r")
print(*file.readlines())