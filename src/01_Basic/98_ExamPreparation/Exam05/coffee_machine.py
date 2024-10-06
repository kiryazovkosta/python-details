DRINK_PRICES = {
    "Espresso": {"Without": 0.90, "Normal": 1.00, "Extra": 1.20 },
    "Cappuccino": {"Without": 1.00, "Normal": 1.20, "Extra": 1.60 },
    "Tea": {"Without": 0.50, "Normal": 0.60, "Extra": 0.70}
}

def get_drink_price(drink, drink_type):
    return DRINK_PRICES[drink][drink_type]

def calculate_discount(drink, drink_type, drinks_count, price ):
    if drink_type == "Without":
        price -= price * 0.35
    if drink == "Espresso" and drinks_count >= 5:
        price -= price * 0.25
    if price > 15:
        price -= price * 0.2
    return price

def main():
    drink = input()
    drink_type = input()
    drinks = int(input())
    drink_price = get_drink_price(drink, drink_type)
    price = drinks * drink_price
    price = calculate_discount(drink, drink_type, drinks, price)
    print(f"You bought {drinks} cups of {drink} for {price:.2f} lv."
)


if __name__ == "__main__":
    main()