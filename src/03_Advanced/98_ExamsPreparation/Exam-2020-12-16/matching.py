from collections import deque

males = [int(n) for n in input().split()]
females = deque([int(n) for n in input().split()])

matches_count = 0
while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        continue

    if males[-1] == females[0]:
        matches_count += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")