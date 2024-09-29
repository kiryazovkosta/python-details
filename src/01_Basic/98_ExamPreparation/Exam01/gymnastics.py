MAXIMUM_POINTS = 20.0

country = input()
tool = input()

points = 0
if country == "Russia":
    if tool == "ribbon":
        points =  9.100 + 9.400
    elif tool == "hoop":
        points =  9.300 + 9.800
    else:
        points = 9.600 + 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        points =  9.600 + 9.400
    elif tool == "hoop":
        points =  9.550 + 9.750
    else:
        points = 9.500 + 9.400
else:
    if tool == "ribbon":
        points =  9.200 + 9.500
    elif tool == "hoop":
        points =  9.450 + 9.350
    else:
        points = 9.700 + 9.150

print(f"The team of {country} get {points:.3f} on {tool}.")
print(f"{100 - (points / MAXIMUM_POINTS * 100):.2f}%")