import math

def closest_to_origin(x1, y1, x2, y2):
    def distance(x, y):
        return math.sqrt(x**2 + y**2)

    # Calculate distances from the origin
    dist1 = distance(x1, y1)
    dist2 = distance(x2, y2)

    # Compare distances and format the result to the lower integer
    if dist1 <= dist2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


x1 = float(input()) 
y1 = float(input())
x2 = float(input())
y2 = float(input())
closest_to_origin(x1, y1, x2, y2)