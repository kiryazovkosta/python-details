import re
from utils import read_input, close_input

file = read_input("input03.txt")
content = file.read()

total = 0
enabled = True
pattern = r"((?:do|don't|mul))\((?:(\d{1,3}),(\d{1,3}))?\)"
matches = re.findall(pattern, content)
for match in matches:
    (oper, first, second) = match
    if oper == "do":
        enabled = True
    elif oper == "don't":
        enabled = False
    else:
        if enabled:
            total += (int(first) * int(second))

print(total)

close_input(file)