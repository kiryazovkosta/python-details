x = float(input())
y = float(input())
h = float(input())

walls_area = (2 * x * x - (1.2 * 2)) + ( 2 * x * y - 2 *(1.5 * 1.5))
walls_paint = walls_area / 3.4
print(f"{walls_paint:.2f}")

roof_area = (2 * x * y) + (2 * (x * h /2))
roof_paint = roof_area / 4.3
print(f"{roof_paint:.2f}")