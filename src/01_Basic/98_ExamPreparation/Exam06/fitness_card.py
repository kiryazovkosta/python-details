SPORTS = {
    "Gym": { "m": 42, "f": 35 },
    "Boxing": { "m": 41, "f": 37 },
    "Yoga": { "m": 45, "f": 42 },
    "Zumba": { "m": 34, "f": 31 },
    "Dances": { "m": 51, "f": 53 },
    "Pilates": { "m": 39, "f": 37 },
}

budget = float(input())
gender = input()
ages = int(input())
sport = input()

sport_price = SPORTS[sport][gender]
if ages <= 19:
    sport_price -= sport_price * 0.2

diff = budget - sport_price
if diff >= 0:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(diff):.2f} more.")