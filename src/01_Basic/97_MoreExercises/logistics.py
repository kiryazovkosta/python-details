boxes = int(input())

train = 0
truck = 0
mini = 0
for box in range(boxes):
    weight = int(input())
    if weight >= 12:
        train += weight
    elif 4 <= weight <= 11:
        truck += weight
    else:
        mini += weight
total_weight = train + truck + mini
average_price = (train * 120 + truck * 175 + mini * 200)/total_weight

print(f"{average_price:.2f}")
print(f"{mini/total_weight*100:.2f}%")
print(f"{truck/total_weight*100:.2f}%")
print(f"{train/total_weight*100:.2f}%")