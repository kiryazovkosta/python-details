from collections import deque

bombs_list = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

created = { value: 0 for key, value in bombs_list.items()}
all_created = False

bombs = deque([int(n) for n in input().split(", ")])
casings = [int(n) for n in input().split(", ")]

while bombs and casings:
    bomb = bombs[0]
    casing = casings[-1]
    mix_sum = bomb + casing
    if mix_sum in bombs_list:
        if bombs_list[mix_sum] not in created:
            created[bombs_list[mix_sum]] = 0
        created[bombs_list[mix_sum]] += 1
        bombs.popleft()
        casings.pop()
    else:
        bombs[0] -= 5

    if len([value for key, value in created.items() if value >= 3]) == 3:
        all_created = True
        break

if all_created:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bombs:
    print(f"Bomb Effects: {', '.join(map(str, bombs))}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")

for key, count in sorted(created.items(), key=lambda kvp: kvp[0]):
    print(f"{key}: {count}")
