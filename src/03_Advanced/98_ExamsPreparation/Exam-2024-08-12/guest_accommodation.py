def accommodate(*args, **kwargs):
    groups = args
    rooms = sorted(kwargs.items(), key=lambda kvp: (kvp[1], kvp[0]))

    accommodates = {}
    unaccommodated = 0
    for group in groups:
        need_accommodate = True
        found_room = False
        for room in rooms:
            if group == room[1]:
                accommodates[room[0].split("_")[1]] = group
                rooms.remove(room)
                need_accommodate = False
                found_room = True
                break
        if need_accommodate:
            for room in rooms:
                if group < room[1]:
                    accommodates[room[0].split("_")[1]] = group
                    rooms.remove(room)
                    found_room = True
                    break
        if not found_room:
            unaccommodated += group
    result = []
    if accommodates:
        result.append(f"A total of {len(accommodates)} accommodations were completed!")
        for r, g in sorted(accommodates.items(), key=lambda kvp: (kvp[0])):
            result.append(f"<Room {r} accommodates {g} guests>")
    else:
        result.append("No accommodations were completed!")

    if unaccommodated > 0:
        result.append(f"Guests with no accommodation: {unaccommodated}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")
    return "\n".join(result)

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print("======================================")
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print("======================================")
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
print("======================================")