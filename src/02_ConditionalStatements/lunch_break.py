from math import ceil

name = input()
duration = int(input())
relax = int(input())

lunch = relax * (1/8)
rest = relax * 0.25
total = relax - lunch - rest
if total >= duration:
    print(f"You have enough time to watch {name} and left with {ceil(total-duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(abs(total-duration))} more minutes.")