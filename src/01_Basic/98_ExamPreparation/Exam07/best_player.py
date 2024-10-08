best_player_goals = 0
best_player_name = ""

while True:
    player_name = input()
    if player_name == "END":
        break

    player_goals = int(input())
    if player_goals > best_player_goals:
        best_player_name = player_name
        best_player_goals = player_goals

    if best_player_goals >= 10:
        break

print(f"{best_player_name} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")