
def get_price_per_km(distance, period):
    if distance >= 100:
        return 0.06
    elif distance >= 20:
        return 0.09
    else:
        if period == "day":
            return 0.79
        else:
            return 0.90

def get_start_price(distance):
    if distance < 20:
        return 0.70
    return 0

def print_result(result: float):
    print(f"{result:.2f}")

def run():
    distance = int(input())
    period = input()
    price_per_km = get_price_per_km(distance, period)
    start_price = get_start_price(distance)
    price = start_price + distance * price_per_km
    print_result(price)


if __name__ == '__main__':
    run()
