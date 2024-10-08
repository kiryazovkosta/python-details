from math import pi, pow, radians

radius = float(input())

area = pi * pow(radius, 2)
perimeter =2 * pi * radius
print(f"{area:.2f}")
print(f"{perimeter:.2f}")