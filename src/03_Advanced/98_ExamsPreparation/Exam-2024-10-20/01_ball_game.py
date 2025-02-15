from collections import deque

strengths = [int(n) for n in input().split()]
accuracies = deque(int(n) for n in input().split())

scored_goals = 0
while strengths and accuracies:
    power_sum = strengths[-1] + accuracies[0]
    if power_sum == 100:
        strengths.pop()
        accuracies.popleft()
        scored_goals += 1
    elif power_sum < 100:
        if strengths[-1] < accuracies[0]:
            strengths.pop()
        elif strengths[-1] > accuracies[0]:
            accuracies.popleft()
        else:
            strengths[-1] = power_sum
            accuracies.popleft()
    elif power_sum > 100:
        strengths[-1] -= 10
        accuracies.append(accuracies.popleft())

if scored_goals == 0:
    print("Paul failed to score a single goal.")
elif 1 <= scored_goals < 3:
    print("Paul failed to make a hat-trick.")
elif scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals > 3:
    print("Paul performed remarkably well!")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if strengths:
    print(f"Strength values left: {', '.join(map(str,strengths))}")
if accuracies:
    print(f"Accuracy values left: {', '.join(map(str,accuracies))}")