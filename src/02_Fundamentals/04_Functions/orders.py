PRODUCTS = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00,
}

def calc_price(product: str, count: int) -> float:
    if product not in PRODUCTS:
        raise ValueError("Ivalid product name")
    
    return PRODUCTS[product] * count

def main():
    product = input()
    count = int(input())
    print(f"{calc_price(count=count, product=product):.2f}")

if __name__ == "__main__":
    main()