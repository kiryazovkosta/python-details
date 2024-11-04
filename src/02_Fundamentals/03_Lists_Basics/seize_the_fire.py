fire_levels = input().split("#")
water = int(input())
effort = 0
used_water = 0
print("Cells:")
for file_level in fire_levels:
    fire_data = file_level.split(" = ")
    level = fire_data[0]
    value = int(fire_data[1])
    if ((level == "High" and (81 <= value <= 125))
            or (level == "Medium" and (51 <= value <= 80))
            or (level == "Low" and (1 <= value <= 50))):
        if used_water + value > water:
            continue
        effort += value * 0.25
        used_water += value
        print(f" - {value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {used_water}")