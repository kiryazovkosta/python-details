from collections import deque

effects = deque([int(n) for n in input().split(", ")])
powers = [int(n) for n in input().split(", ")]

palm = 0
willow = 0
crossette = 0

while effects and powers:
    effect = effects.popleft()
    power = powers.pop()

    if effect <= 0:
        powers.append(power)
        continue

    if power <= 0:
        effects.appendleft(effect)
        continue

    current_sum = effect + power
    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palm += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        willow += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette += 1
    else:
        effect -= 1
        effects.append(effect)
        powers.append(power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        break

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if powers:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")


