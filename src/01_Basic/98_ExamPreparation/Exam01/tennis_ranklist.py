from math import floor

tournament_count = int(input())
points = int(input())

tournament_points = 0
wins = 0

for _ in range(0, tournament_count):
    stage = input()
    if stage == "W":
        tournament_points += 2000
        wins += 1
    elif stage == "F":
        tournament_points += 1200
    else:
        tournament_points += 720

print(f"Final points: {points + tournament_points}")
print(f"Average points: {floor(tournament_points/tournament_count)}")
print(f"{wins/tournament_count * 100:.2f}%")