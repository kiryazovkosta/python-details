DISCOUNTS = {
    "Thrones": 0.5,
    "Lucifer": 0.4,
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1
}

def discount(serial):
    if serial in DISCOUNTS:
        return DISCOUNTS[serial]
    return 0

def print_result(budget, total_price):
    diff = budget - total_price
    if diff >= 0:
        print(f"You bought all the series and left with {diff:.2f} lv.")
    else:
        print(f"You need {abs(diff):.2f} lv. more to buy the series!")


def main():
    budget = float(input())
    serials = int(input())
    total_serials_price = 0
    for _ in range(serials):
        name = input()
        price = float(input())
        price = price - (price * discount(name))
        total_serials_price += price
    print_result(budget, total_serials_price)

if __name__ == "__main__":
    main()