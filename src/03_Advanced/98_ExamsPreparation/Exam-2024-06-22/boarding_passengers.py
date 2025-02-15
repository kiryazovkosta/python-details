def boarding_passengers(capacity, *args):
    boarded = {}
    unique = set()
    success = 0
    total = sum([int(gr[0]) for gr in args])
    for guests, name in args:
        unique.add(name)
        if guests <= capacity:
            capacity -= guests
            success += guests
            if name not in boarded:
                boarded[name] = 0
            boarded[name] += guests
            if capacity == 0:
                break

    print(len(unique) == len(boarded))
    print(total)
    print(success)
    print(total == success)

    result = ["Boarding details by benefit plan:"]
    for key, value in sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        result.append(f"## {key}: {value} guests")
    if len(unique) == len(boarded) and total == success and capacity == 0:
        result.append("All passengers are successfully boarded!")
    elif capacity == 0 and total > success:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif capacity > 0 and total > success:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")
    return "\n".join(result)






# print(boarding_passengers(150, (35,'Diamond'), (55, 'Platinum'), (35,'Gold'), (25, 'First Cruiser')))
# print("==============================================================")
# print(boarding_passengers(100, (20,'Diamond'), (15, 'Platinum'), (25,'Gold'), (25, 'First Cruiser'), (15,'Diamond'), (10, 'Gold')))
# print("==============================================================")
print(boarding_passengers(120, (30,'Gold'), (20, 'Platinum'), (30,'Diamond'), (10, 'First Cruiser'), (31,'Platinum'), (20, 'Diamond')))
print("==============================================================")


