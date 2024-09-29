DAILY_STEPS_GOAL = 10000

daily_steps = 0

while daily_steps <= DAILY_STEPS_GOAL:
    text = input()
    if text == "Going home":
        last_steps = int(input())
        daily_steps += last_steps
        break
    else:
        steps = int(text)
        daily_steps += steps

if daily_steps >= DAILY_STEPS_GOAL:
    print(f"Goal reached! Good job!\n{daily_steps - DAILY_STEPS_GOAL} steps over the goal!")
else:
    print(f"{DAILY_STEPS_GOAL - daily_steps} more steps to reach goal.")