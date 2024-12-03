import os

current_directory = os.path.join(os.getcwd(), "src/Advent_of_Code/2024")
file_path = os.path.join(current_directory, "input01.txt")
print(file_path)

file = open(file_path, 'r')

first = []
second = []
for line in file.readlines():
    a, b = map(int, line.split())
    first.append(a)
    second.append(b)

total_distance = 0
first.sort()
second.sort()
for idx in range(0, len(first)):
    total_distance += abs(first[idx] - second[idx])

print(total_distance)