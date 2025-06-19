from collections import deque

def main():
    bombs = {
        40: "DaturaBomb",
        60: "CherryBomb",
        120: "SmokeDecoyBomb"
    }

    created = False
    datura_bombs = 0
    cherry_bombs = 0
    smoke_decoy_bombs = 0

    effects =  deque([int(n) for n in input().split(", ")])
    casings =([int(n) for n in input().split(", ")])

    while effects and casings:
        effect = effects.popleft()
        casing = casings.pop()

        current_bomb = effect + casing
        if current_bomb == 40:
            datura_bombs += 1
        elif current_bomb == 60:
            cherry_bombs += 1
        elif current_bomb == 120:
            smoke_decoy_bombs += 1
        else:
            effects.appendleft(effect - 5)
            casings.append(casing)

        if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
            created = True
            break
    if created:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    if effects:
        print(f"Bomb Effects: {', '.join([str(e) for e in effects])}")
    else:
        print("Bomb Effects: empty")

    if casings:
        print(f"Bomb Casings: {', '.join([str(c) for c in casings])}")
    else:
        print("Bomb Casings: empty")

    print(f"Cherry Bombs: {cherry_bombs}\nDatura Bombs: {datura_bombs}\nSmoke Decoy Bombs: {smoke_decoy_bombs}")

if __name__ == "__main__":
    main()