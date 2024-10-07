minutes:int = int(input())
trips:int = int(input())
calories: int = int(input())

burned_calories = minutes * trips * 5
daily = burned_calories/calories * 100
if daily >= 50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")

