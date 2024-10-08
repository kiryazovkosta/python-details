from math import floor

count = int(input())
points = 0
redCounter = 0
orangeCounter = 0
yellowCounter = 0
whiteCounter = 0
blackCounter = 0
otherCounter = 0
for _ in range(count):
    color = input()
    if color == "red":
        points += 5
        redCounter += 1
    elif color == "orange":
        points += 10
        orangeCounter += 1
    elif color == "yellow":
        points += 15
        yellowCounter += 1
    elif color == "white":
        points += 20
        whiteCounter += 1
    elif color == "black" :
        points = floor(points/2)
        blackCounter += 1
    else:
        otherCounter += 1

print(f"Total points: {points}")
print(f"Red balls: {redCounter}")
print(f"Orange balls: {orangeCounter}")
print(f"Yellow balls: {yellowCounter}")
print(f"White balls: {whiteCounter}")
print(f"Other colors picked: {otherCounter}")
print(f"Divides from black balls: {blackCounter}")