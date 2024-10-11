capacity = int(input())
fans = int(input())

aCounter = 0
bCounter = 0
vCounter = 0
gCounter = 0
for _ in range(fans):
    sector = input()
    if sector == "A":
        aCounter += 1
    elif sector == "B":
        bCounter += 1
    elif sector == "V":
        vCounter += 1
    else:
        gCounter += 1

total = aCounter + bCounter + vCounter + gCounter
print(f"{aCounter/total*100:.2f}%")
print(f"{bCounter/total*100:.2f}%")
print(f"{vCounter/total*100:.2f}%")
print(f"{gCounter/total*100:.2f}%")
print(f"{total/capacity*100:.2f}%")