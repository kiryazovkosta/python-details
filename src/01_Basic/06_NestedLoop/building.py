floors = int(input())
rooms = int(input())

for floor_index in range(floors, 0, -1):
    for room_index in range(0, rooms):
        if floor_index == floors:
            print(f"L{floor_index}{room_index}", end=" ")
        elif floor_index % 2 == 0:
            print(f"O{floor_index}{room_index}", end=" ")
        else:
            print(f"A{floor_index}{room_index}", end=" ")
    print()