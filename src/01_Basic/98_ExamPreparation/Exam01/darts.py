player_name = input()

player_points=  301
successful_shots = 0
unsuccessful_shots = 0
while player_points > 0:
    field = input()
    if field == "Retire":
        break

    points = int(input())
    if field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3

    if player_points >= points:
        successful_shots += 1
        player_points -= points
    else:
        unsuccessful_shots += 1

if player_points == 0:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")