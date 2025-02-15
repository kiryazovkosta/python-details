from collections import deque

colors_strings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []
while colors_strings:
    first = colors_strings.popleft()
    last = collected_colors.pop() if colors_strings else ""