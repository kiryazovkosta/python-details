FUEL_PRICES = {
    "Gasoline": { "Price": 2.22, "Discount": 0.18 },
    "Diesel":  { "Price": 2.33, "Discount": 0.12 },
    "Gas": { "Price": 0.93, "Discount": 0.08 },
}

def get_fuel_price_per_liter(fuel, has_club_card):
    price = FUEL_PRICES[fuel]["Price"]
    if has_club_card.lower() == "yes":
        price -= FUEL_PRICES[fuel]["Discount"]
    return price

def main():
    fuel = input()
    quantity = float(input())
    has_club_card = input()

    fuel_price_per_liter = get_fuel_price_per_liter(fuel, has_club_card)
    price = quantity * fuel_price_per_liter
    if quantity > 25:
        price -= price * 0.1
    elif 20 <= quantity <= 25:
        price -= price * 0.08
    print(f"{price :.2f} lv.")

if __name__ == "__main__":
    main()