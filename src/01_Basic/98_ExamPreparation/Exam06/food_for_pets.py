days = int(input())
food = float(input())

biscuits = 0
total_dog_food = 0
total_cat_food = 0
for dayIndex in range(1, days + 1):
    dog_food = float(input())
    cat_food = float(input())
    daily_food = dog_food + cat_food
    if dayIndex % 3 == 0:
        biscuits += daily_food * 0.1
    total_dog_food += dog_food
    total_cat_food += cat_food

total_food = total_dog_food + total_cat_food
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food/food*100:.2f}% of the food has been eaten.")
print(f"{total_dog_food/total_food*100:.2f}% eaten from the dog.")
print(f"{total_cat_food/total_food*100:.2f}% eaten from the cat.")