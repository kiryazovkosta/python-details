first_team = [num for num in range(1, 12)]
second_team = [num for num in range(1, 12)]

game_terminated = False
cards = [card.split("-") for card in input().split(" ")]
for card in cards:
    player = int(card[1])
    if card[0] == "A" and player in first_team:
        first_team.remove(player)
    elif card[0] == "B" and player in second_team:
        second_team.remove(player)
        
    if len(first_team) < 7 or len(second_team) < 7:
        game_terminated = True
        break

print(f"Team A - {len(first_team)}; Team B - {len(second_team)}")
if game_terminated:
    print("Game was terminated")