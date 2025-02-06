def plant_garden(space, *args, **kwargs):
    allowed_plants = dict(args)
    plants = sorted(kwargs.items(), key = lambda kvp: (kvp[0]))

    total_planted = 0
    real_planted = 0
    planted = []

    for plant, quantity in plants:
        if plant in allowed_plants:
            total_planted += quantity
            single_space = allowed_plants[plant]
            total_space = quantity * single_space
            if total_space <= space:
                planted.append((plant, quantity))
                space -= total_space
                real_planted += quantity
            else:
                pieces = space // single_space
                if pieces > 0:
                    space = space % single_space
                    planted.append((plant, int(pieces)))
                    real_planted += pieces
            if space <= 0:
                break

    result = []
    unique = set(allowed_plants.keys()) & set(kwargs.keys())
    if total_planted == real_planted and len(planted) == len(unique):
        result.append(f"All plants were planted! Available garden space: {space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    result.append("Planted plants:")
    for p, s in planted:
        result.append(f"{p}: {s}")

    return "\n".join(result)

print(plant_garden(50.0,("rose", 2.5), ("tulip",1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0,("rose", 2.0), ("tulip",1.2), ("sunflower", 3.0),rose=10, tulip=20,sunflower=5))
print(plant_garden(2.0,("rose", 2.5), ("tulip",1.2), ("daisy", 0.2),rose=4, tulip=15,sunflower=3, daisy=4))
print(plant_garden(50.0,("tulip", 1.2),("sunflower", 3.0),rose=10, tulip=20,daisy=1))