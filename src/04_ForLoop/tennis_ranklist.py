from math import floor

tours = int(input())
points = int(input())
added_points = 0
winner = 0
for i in range(0, tours):
    stage = input()
    if stage == "W":
        added_points += 2000
        winner += 1
    elif stage == "F":
        added_points += 1200
    elif stage == "SF":
        added_points += 720

print(f"Final points: {points + added_points}")
print(f"Average points: {floor(added_points / tours)}")
print(f"{winner/tours * 100:.2f}%")
