MAXIMUM_NEEDED_POINTS = 1250.5

actor = input()
points = float(input())
jury = int(input())

for _ in range(jury):
    name = input()
    point = float(input())
    points += (len(name) * point)/2

    if points > MAXIMUM_NEEDED_POINTS:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        break
else:
    needed = MAXIMUM_NEEDED_POINTS - points
    print(f"Sorry, {actor} you need {needed:.1f} more!")