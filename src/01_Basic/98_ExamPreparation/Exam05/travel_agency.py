PACKAGES_PRICE = {
    "Bansko": {"withEquipment": {"price": 100, "vip": 10} ,"noEquipment": {"price": 80, "vip": 5} },
    "Borovets": {"withEquipment": {"price": 100, "vip": 10} ,"noEquipment": {"price": 80, "vip": 5} },
    "Varna": {"withBreakfast": {"price": 130, "vip": 12} ,"noBreakfast": {"price": 100, "vip": 7} },
    "Burgas": {"withBreakfast": {"price": 130, "vip": 12} ,"noBreakfast": {"price": 100, "vip": 7} }
}

def are_days_valid(days):
    return True if days >= 1 else False

def validate_input(city, package_type):
    if city in PACKAGES_PRICE:
        if package_type in PACKAGES_PRICE[city]:
            return True
    return False

def get_daily_price(city, package_type):
    return PACKAGES_PRICE[city][package_type]["price"]

def get_vip_discount(city, package_type):
    return PACKAGES_PRICE[city][package_type]["vip"]

def main():
    city = input()
    package_type = input()
    is_vip = input()
    days = int(input())
    is_days_valid = are_days_valid(days)
    if not is_days_valid:
        print("Days must be positive number!")
        return

    is_input_valid = validate_input(city, package_type)
    if not is_input_valid:
        print("Invalid input!")
        return

    if days > 7:
        days -= 1

    daily_price = get_daily_price(city, package_type)
    price = days * daily_price
    if is_vip == "yes":
        vip_discount = get_vip_discount(city, package_type=package_type)
        price -= price * vip_discount/100
    print(f"The price is {price:.2f}lv! Have a nice time!")

if __name__ == "__main__":
    main()