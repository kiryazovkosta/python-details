import sys

max_ascii_points = -sys.maxsize
max_ascii_point_movie = ""

for _ in range(0, 7):
    ascii_points = 0
    name = input()
    if name == "STOP":
        break

    length = len(name)
    for ch in name:
        points = ord(ch)
        if ch.islower():
            points -= length * 2
        elif ch.isupper():
            points -= length
        ascii_points += points
    if ascii_points > max_ascii_points:
        max_ascii_points = ascii_points
        max_ascii_point_movie = name
else:
    print("The limit is reached.")

print(f"The best movie for you is {max_ascii_point_movie} with {max_ascii_points} ASCII sum.")