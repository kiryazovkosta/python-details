from collections import deque

packages = [int(p) for p in input().split()]
couriers = deque([int(c) for c in input().split()])

total_delivery_weight = 0
while packages and couriers:
    current_package = packages[-1]
    current_courier = couriers[0]
    if current_courier >= current_package:
        capacity = current_courier -current_package * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_delivery_weight += packages.pop()
    else:
        packages[-1] -= couriers.popleft()
        total_delivery_weight += current_courier

print(f"Total weight: {total_delivery_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(p) for p in packages)}")
elif couriers:
    print(f"Couriers are still on duty: {', '.join(str(c) for c in couriers)} but there are no more packages to deliver.")