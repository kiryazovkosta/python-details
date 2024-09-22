from dbm import error

def boat_price_per_season(season_name: str):
    if season_name == "Spring":
        return 3000
    elif season_name == "Summer" or season_name == "Autumn":
        return 4200
    elif season_name == "Winter":
        return 2600
    else:
        raise ValueError("Invalid season. Please enter Spring, Summer, Autumn, or Winter.")

def discount_per_fishermen_count(count: int):
    if count <= 6:
        return 0.1
    elif 7 <= count <= 11:
        return 0.15
    else:
        return 0.25

def even_fishermen_discount(season_name: str, count: int ):
    if season_name != "Autumn" and count % 2 == 0:
        return True
    return False


budget = int(input())
season = input()
fisherman_count = int(input())

amount_price = boat_price_per_season(season)
discount_percentages = discount_per_fishermen_count(fisherman_count)
amount_price -= (amount_price * discount_percentages)
if even_fishermen_discount(season, fisherman_count):
    amount_price -= amount_price * 0.05

balance = budget - amount_price
if balance >= 0:
    print(f"Yes! You have {balance:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(balance):.2f} leva.")