hops = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
points = 0
for _ in range(hops):
    number = int(input())
    if 0 <= number <= 9:
        p1 += 1
        points += number * 0.20
    elif 10 <= number <= 19:
        p2 += 1
        points += number * 0.30
    elif 20 <= number <= 29:
        p3 += 1
        points += number * 0.40
    elif 30 <= number <= 39:
        p4 += 1
        points += 50
    elif 40 <= number <= 50:
        p5 += 1
        points += 100
    else:
        p6 += 1
        points /= 2
    
print(f"{points:.2f}")
print(f"From 0 to 9: {p1/hops*100:.2f}%")
print(f"From 10 to 19: {p2/hops*100:.2f}%")
print(f"From 20 to 29: {p3/hops*100:.2f}%")
print(f"From 30 to 39: {p4/hops*100:.2f}%")
print(f"From 40 to 50: {p5/hops*100:.2f}%")
print(f"Invalid numbers: {p6/hops*100:.2f}%")