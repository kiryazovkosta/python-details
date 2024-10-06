import sys

max_points = -sys.maxsize
max_name = ""

name = ""
while True:
    name = input()
    if name == "Stop":
        break

    player_point = 0
    for ch in name:
         number = int(input())
         if ord(ch) == number:
             player_point += 10
         else:
            player_point += 2

    if player_point >= max_points:
        max_points = player_point
        max_name = name

print(f"The winner is {max_name} with {max_points} points!")