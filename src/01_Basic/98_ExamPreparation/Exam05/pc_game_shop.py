HEARTHSTONE = "Hearthstone"
FORNITE = "Fornite"
OVERWATCH = "Overwatch"
OTHERS = "Others"

games = {
    HEARTHSTONE: 0,
    FORNITE: 0,
    OVERWATCH: 0,
    OTHERS: 0
}

games_count = int(input())

for _ in range(games_count):
    game = input()
    if game in games:
        games[game] += 1
    else:
        games["Others"] += 1

print(f"{HEARTHSTONE} - {games.get(HEARTHSTONE)/games_count*100:.2f}%")
print(f"{FORNITE} - {games.get(FORNITE)/games_count*100:.2f}%")
print(f"{OVERWATCH} - {games.get(OVERWATCH)/games_count*100:.2f}%")
print(f"{OTHERS} - {games.get(OTHERS)/games_count*100:.2f}%")