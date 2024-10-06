
from math import ceil
height = int(input())
width = int(input())
non_paint = int(input())

total_area = height * width * 4
total_area -= total_area * (non_paint/100)
painted_area = 0
while True:
    liters = input()
    if liters == "Tired!":
        print(f"{ceil(total_area - painted_area)} quadratic m left.")
        break

    liters = int(liters)
    painted_area += liters
    if painted_area == total_area:
        print(f"All walls are painted! Great job, Pesho!")
        break
    elif painted_area > total_area:
        print(f"All walls are painted and you have {ceil(painted_area - total_area)} l paint left!")
        break
