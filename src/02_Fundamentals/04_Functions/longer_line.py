import math 
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def longer_line():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())

    distance1 = distance(x1, y1, x2, y2)
    distance2 = distance(x3, y3, x4, y4)

    print(distance1)
    print(distance2)

longer_line()