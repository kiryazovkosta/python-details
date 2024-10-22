calculate_price = lambda capsules, price_per_capsule, days : capsules * price_per_capsule * days

def validate(capsules, price_per_capsule, days) -> bool:
    if not 0.01 <= price_per_capsule <= 100.00:
        return False
    if not 1 <= days <= 31:
        return False
    if not 1 <= capsules <= 2000:
        return False
    
    return True
    


def main():
    total_price = 0.00
    orders = int(input())
    for _ in range(orders):
        price_per_capsule = float(input())
        days = int(input())
        capsules = int(input())
        if not validate(capsules, price_per_capsule, days):
            continue

        price = calculate_price(capsules, price_per_capsule, days)
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
    print(f"Total: ${total_price:.2f}")

if __name__ == "__main__":
    main()