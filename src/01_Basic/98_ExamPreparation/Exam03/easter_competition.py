import sys
participants = int(input())
maximum_points = -sys.maxsize
maximum_points_owner = ""
for _ in range(participants):
    total_points = 0

    name = input()
    while True:
        points = input()
        if points == "Stop":
            print(f"{name} has {total_points} points.")
            if total_points > maximum_points:
                maximum_points = total_points
                maximum_points_owner = name
                print(f"{name} is the new number 1!")
            break

        total_points += int(points)

print(f"{maximum_points_owner} won competition with {maximum_points} points!")