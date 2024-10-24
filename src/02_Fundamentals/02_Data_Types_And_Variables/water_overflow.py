CAPACITY = 255

n = int(input())
filled_capacity = 0
for _ in range(n):
    liters = int(input())
    if liters + filled_capacity > CAPACITY:
        print("Insufficient capacity!")
    else:
        filled_capacity += liters

print(filled_capacity)