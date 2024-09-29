degree_celsius = int(input())
time_of_day = input()

outfit = "Shirt"
shoes = "Moccasins"

match time_of_day:
    case "Morning":
        if 10<= degree_celsius <= 18:
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        elif 18 < degree_celsius <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        else:
            outfit = "T-Shirt"
            shoes = "Sandals"

    case "Afternoon":
        if 10 <= degree_celsius <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif 18 < degree_celsius <= 24:
            outfit = "T-Shirt"
            shoes = "Sandals"
        else:
            outfit = "Swim Suit"
            shoes = "Barefoot"

print(f"It's {degree_celsius} degrees, get your {outfit} and {shoes}.")