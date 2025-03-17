def reverse_text(text: str):
    for index in range(len(text) - 1, -1, -1):
        yield text[index]

def reverse_text_s(text: str):
    for ch in reversed(text):
        yield ch

for char in reverse_text("step"):
    print(char, end='')

print()
for char in reverse_text_s("step"):
    print(char, end='')