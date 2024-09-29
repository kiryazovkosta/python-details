budget = float(input())
season = input()

destination = "Europe"
trip_type = "Hotel"
price = 0.9

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip_type = "Camp"
        price = 0.3
    else:
        price = 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip_type = "Camp"
        price = 0.4
    else:
        price = 0.8

print(f"Somewhere in {destination}")
print(f"{trip_type} - {budget*price:.2f}")