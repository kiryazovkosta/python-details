PRICE_FOOD_FOR_DOGS = 2.5
PRICE_FOOD_FOR_CATS = 4.0

dog_packs = int(input())
cat_packs = int(input())

total_price = ((dog_packs * PRICE_FOOD_FOR_DOGS)
                   + (cat_packs * PRICE_FOOD_FOR_CATS))
print(f'{total_price} lv.')