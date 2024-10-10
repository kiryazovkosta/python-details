FUEL_PRICES = {
    "Gasoline": { "Price": 2.22, "Discount": 0.18 },
    "Diesel":  { "Price": 2.33, "Discount": 0.12 },
    "Gas": { "Price": 0.93, "Discount": 0.08 },
}

def read_input():
    fuel = input()
    quantity = float(input())
    has_club_card = input()
    return fuel, has_club_card, quantity

def get_fuel_price_per_liter(fuel, has_club_card):
    price = FUEL_PRICES[fuel]["Price"]
    if has_club_card.lower() == "yes":
        price -= FUEL_PRICES[fuel]["Discount"]
    return price

def calculate_discount(price, quantity):
    """
    Calculate discount of price depending on fuel's quantity
    :param price: Price of fuel
    :param quantity: Quantity of fuel
    :return: Price of fuel with applies discount
    """
    if quantity > 25:
        price -= price * 0.1
    elif 20 <= quantity <= 25:
        price -= price * 0.08
    return price

def main():
    fuel, has_club_card, quantity = read_input()

    fuel_price_per_liter = get_fuel_price_per_liter(fuel, has_club_card)
    price = quantity * fuel_price_per_liter
    price = calculate_discount(price, quantity)
    print(f"{price :.2f} lv.")

if __name__ == "__main__":
    main()