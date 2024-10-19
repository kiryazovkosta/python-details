budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg + flour_price_per_kg * 0.25

bread_price = flour_price_per_kg + eggs_price_per_pack + (milk_price_per_liter * 0.25)

breads = 0
colored_eggs = 0
while budget > bread_price:
    breads += 1
    colored_eggs += 3
    if breads % 3 == 0:
        colored_eggs -= breads - 2
    budget -= bread_price

print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
