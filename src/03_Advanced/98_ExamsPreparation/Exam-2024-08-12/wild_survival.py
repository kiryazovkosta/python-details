from collections import deque

BEES_KILLED_BY_BEE_EATER = 7

bees = deque([int(b) for b in input().split()])
bee_eaters = [int(be) for be in input().split()]
while bees and bee_eaters:
    current_bees = bees.popleft()
    current_bee_eaters = bee_eaters.pop()
    while current_bees > 0 and current_bee_eaters > 0:
        current_bees -= BEES_KILLED_BY_BEE_EATER
        if current_bees >= 0:
            current_bee_eaters -= 1

    if current_bees > 0:
        bees.append(current_bees)
    elif current_bee_eaters > 0:
        bee_eaters.append(current_bee_eaters)


print("The final battle is over!")
if bees:
    print(f"Bee groups left: {', '.join(str(b) for b in bees)}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(be) for be in bee_eaters)}")
else:
    print("But no one made it out alive!")