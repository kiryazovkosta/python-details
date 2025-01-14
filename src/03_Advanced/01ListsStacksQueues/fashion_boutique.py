clothes_in_box = [int(c) for c in input().split()]
rack_capacity = int(input())

racks = 1 if clothes_in_box else 0
current_rack_capacity = 0

while clothes_in_box:
    clothes = clothes_in_box.pop()
    if clothes + current_rack_capacity < rack_capacity:
        current_rack_capacity += clothes
    elif clothes + current_rack_capacity == rack_capacity:
        racks += 1
        current_rack_capacity = 0
    else:
        racks += 1
        current_rack_capacity = clothes

print(racks)