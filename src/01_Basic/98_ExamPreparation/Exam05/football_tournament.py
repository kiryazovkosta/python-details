team = input()
games = int(input())

win_counter = 0
draw_counter = 0
loss_counter = 0
for _ in range(games):
    score = input().lower()
    if score == "w":
        win_counter += 1
    elif score == "d":
        draw_counter += 1
    else:
        loss_counter += 1

if games == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {win_counter * 3 + draw_counter} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {draw_counter}")
    print(f"## L: {loss_counter}")
    print(f"Win rate: {win_counter/games*100:.2f}%")