from collections import deque

contestants = deque([int(n) for n in input().split()])
pies = [int(n) for n in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()
    if contestant >= pie:
        quantity = contestant - pie
        if quantity > 0:
            contestants.append(quantity)
    else:
        quantity = pie - contestant
        if pies and quantity == 1:
            pies[-1] += quantity
        else:
            pies.append(quantity)

if not contestants and not pies:
    print("We have a champion!")
if contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")
if pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(p) for p in pies])}")
