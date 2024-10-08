def get_price_and_discount(joinery_type, count):
    pricing_data = {
        "90X130": {"price": 110, "discount_thresholds": [(60, 0.08), (30, 0.05)]},
        "100X150": {"price": 140, "discount_thresholds": [(80, 0.10), (40, 0.06)]},
        "130X180": {"price": 190, "discount_thresholds": [(50, 0.12), (20, 0.07)]},
        "200X300": {"price": 250, "discount_thresholds": [(50, 0.14), (25, 0.09)]}
    }

    if joinery_type in pricing_data:
        price = pricing_data[joinery_type]["price"]
        discount_thresholds = pricing_data[joinery_type]["discount_thresholds"]
    else:
        raise ValueError(f"Invalid joinery type: {joinery_type}")

    discount = 0
    for threshold, discount_value in discount_thresholds:
        if count > threshold:
            discount = discount_value
            break

    return price, discount

def main():
    count = int(input())
    joinery_type = input()
    delivery_type = input()

    if count < 10:
        print(f"Invalid order")
        return

    price, discount = get_price_and_discount(joinery_type, count)
    total_price = count * price
    if discount > 0:
        total_price -= total_price * discount
    if delivery_type == "With delivery":
        total_price += 60
    if count >= 100:
        total_price -= total_price * 0.04

    print(f"{total_price:.2f} BGN")


if __name__ == "__main__":
    main()




