input = input()
animals = input.split(", ")
wolf_index = animals.index("wolf")
if wolf_index == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    
    sheep_number = len(animals) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")