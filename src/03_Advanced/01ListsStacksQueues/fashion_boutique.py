clothes = [int(c) for c in input().split()]
rack_capacity = int(input())
racks = 1
current_rack_capacity = rack_capacity

while clothes:
    cloth = clothes.pop()
    if cloth <= current_rack_capacity:
        current_rack_capacity -= cloth  # Place it on the current rack
    else:
        racks += 1  # Need a new rack
        current_rack_capacity = rack_capacity - cloth

print(racks)