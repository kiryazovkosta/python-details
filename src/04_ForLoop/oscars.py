import sys

actor_name = input()
points = float(input())
appraisers = int(input())

for i in range(0, appraisers):
    appraiser_name = input()
    appraiser_points =  float(input())

    points +=  ((len(appraiser_name) * appraiser_points) / 2)
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        sys.exit(0)

print(f"Sorry, {actor_name} you need {(1250.5 - points):.1f} more!")