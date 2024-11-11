times = [int(time) for time in input().split(" ")]
length = len(times)
left = 0
right = 0
for index in range(length // 2):
    left_time = times[index]
    left += left_time
    if left_time == 0:
        left -= left * 0.2

    right_time = times[length - index - 1]
    right += right_time
    if right_time == 0:
        right -= right * 0.2

winner, total_time = ("left", left) if left < right else ("right", right)

print(f"The winner is {winner} with total time: {total_time:.1f}")