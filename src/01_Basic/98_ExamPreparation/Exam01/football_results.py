def game_result(result):
    first_score, second_score = result.split(":")

    first_score = int(first_score)
    second_score = int(second_score)
    if first_score > second_score:
        return 1
    elif second_score > first_score:
        return -1
    else:
        return 0

first_game = input()
second_game = input()
last_game = input()
games = [first_game, second_game, last_game]

wins = 0
loss = 0
draw = 0

for game in games:
    result = game_result(game)
    if result == 1:
        wins += 1
    elif result == -1:
        loss += 1
    else:
        draw += 1

print(f"Team won {wins} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {draw}")