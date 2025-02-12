def cookbook(*args):
    recipes = {}
    for name, cuisine, ingredient in args:
        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append({name: ingredient})

    result = []
    for key, value in sorted(recipes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result.append(f"{key} cuisine contains {len(value)} recipes:")
        recipes_list = {k: v for d in value for k, v in d.items()}
        for name, ingredients in sorted(recipes_list.items(), key = lambda s: (s[0])):
            result.append(f"  * {name} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(result)

# The objective is to sort the recipes by their cuisine, arranging Alex('s collection based on the number of recipes in each cuisine in descending order.
# In cases where two or more cuisines have the same number of recipes, they should be returned in ascending order (alphabetically) by cuisine.)
# Within each cuisine group, the recipes should be sorted in ascending order (alphabetically) by the recipe's name.
# To aid Alex in quickly assessing the number of recipes in each cuisine group, the function should print the count of recipes next to each cuisine.
# Furthermore, for each recipe within a cuisine group, display the necessary ingredients.
# In the end, return the output as described below.

print(
    cookbook(
        ("Spaghetti Bolognese", "Italian",["spaghetti", "tomato sauce", "ground beef"]),
        ("Margherita Pizza", "Italian", ["pizzadough", "tomato sauce", "mozzarella"]),
        ("Tiramisu", "Italian", ["ladyfingers","mascarpone", "coffee"]),
        ("Croissant", "French", ["flour","butter", "yeast"]),
        ("Ratatouille", "French", ["eggplant","zucchini", "tomatoes"]))
)
print("==========================================================")
print(
    cookbook(
        ("Pad Thai", "Thai", ["rice noodles","shrimp", "peanuts", "bean sprouts", "tamarind sauce"]))
)
print("==========================================================")
print(cookbook(
    ("Spaghetti Bolognese", "Italian",["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers","mascarpone", "coffee"]),
    ("Croissant", "French", ["flour","butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"]) )
)
print("==========================================================")