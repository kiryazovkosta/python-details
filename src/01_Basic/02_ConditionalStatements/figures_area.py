from math import pi

figure_type = input()
a = float(input())
area = 0.000
if figure_type == "square":
    area = a * a
elif figure_type == "rectangle":
    b = float(input())
    area = a * b
elif figure_type == "circle":
    area = pi * a**2
elif figure_type == "triangle":
    b = float(input())
    area = (a * b) / 2

print(round(area, 3))