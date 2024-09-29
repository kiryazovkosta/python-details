name = input()

win_games = 0
lost_games = 0
while name != "End of tournaments":
    games = int(input())
    for gameIndex in range(1, games + 1):
        first_team_points = int(input())
        second_team_points = int(input())
        if first_team_points > second_team_points:
            win_games += 1
            print(f"Game {gameIndex} of tournament {name}: win with {first_team_points - second_team_points} points.")
        else:
            lost_games += 1
            print(f"Game {gameIndex} of tournament {name}: lost with {second_team_points - first_team_points} points.")
    name = input()

print(f"{win_games/(win_games+ lost_games) * 100:.2f}% matches win")
print(f"{lost_games/(win_games+ lost_games) * 100:.2f}% matches lost")