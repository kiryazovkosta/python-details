VALID_FUELS = ["Diesel", "Gasoline", "Gas"]
MINIMUM_NON_FILL_QUANTITY = 25

def fuel_is_valid(fuel):
    if fuel in VALID_FUELS:
        return True
    return False

def need_fill(quantity):
    if quantity < MINIMUM_NON_FILL_QUANTITY:
        return True
    else:
        return False

def main():
    fuel = input()
    quantity = float(input())
    if not fuel_is_valid(fuel):
        print("Invalid fuel!")
        return
    if need_fill(quantity):
        print(f"Fill your tank with {fuel.lower()}!")
    else:
        print(f"You have enough {fuel.lower()}.")

if __name__ == "__main__":
    main()