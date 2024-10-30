animal_parts = []
for _ in range(3):
    animal_parts.append(input())

animal_parts[0], animal_parts[2] = animal_parts[2], animal_parts[0]

print(animal_parts)
