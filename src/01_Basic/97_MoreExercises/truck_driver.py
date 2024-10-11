

def get_price_per_kilometer(season, distance):
    price_per_km = 0
    if 10000 < distance <= 20000:
        price_per_km = 1.45
    elif 5000 < distance <= 10000:
        if season == "Winter":
            price_per_km = 1.25
        elif season == "Summer":
            price_per_km = 1.10
        else:
            price_per_km = 0.95
    else:
        if season == "Winter":
            price_per_km = 1.05
        elif season == "Summer":
            price_per_km = 0.90
        else:
            price_per_km = 0.75
    return price_per_km

def main():
    season = input()
    distance = float(input())
    price_per_km = get_price_per_kilometer(season, distance)
    salary = 4 * distance * price_per_km
    salary -= salary * 0.10
    print(f"{salary:.2f}")

if __name__ == "__main__":
    main()