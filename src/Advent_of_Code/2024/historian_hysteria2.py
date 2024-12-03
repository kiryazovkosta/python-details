import os

current_directory = os.path.join(os.getcwd(), "src/Advent_of_Code/2024")
file_path = os.path.join(current_directory, "input01.txt")
print(file_path)

file = open(file_path, 'r')

first = []
second = {}
for line in file.readlines():
    a, b = map(int, line.split())
    first.append(a)
    if b in second:
        second[b] += 1
    else:
        second[b] = 1

similarity_score = 0

for idx in range(0, len(first)):
    similarity_score += first[idx] * second[first[idx]] if first[idx] in second else 0

print(similarity_score)