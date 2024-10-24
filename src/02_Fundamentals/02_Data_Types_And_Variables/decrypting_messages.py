key = int(input())
lines = int(input())

letters = list()
for _ in range(lines):
    letters.append(chr(ord(input()) + key))

print("".join(letters))